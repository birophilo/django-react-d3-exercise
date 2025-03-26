from django.db.models import Count, Q
from django.db.models.functions import TruncMonth, TruncYear
from django.http import JsonResponse

from rest_framework.decorators import api_view
# from rest_framework.response import Response

from feedback.models import CustomerFeedback
from feedback.serializers import (
    CustomerFeedbackSerializer,
    CustomerFeedbackAnnotatedSerializer
)


@api_view(['GET'])
def feedback(request):

    params = request.GET

    group_by = params.get('groupBy', None)
    country_code = params.get('countryCode', None)
    feedback_subcategory = params.get('feedbackSubcategory', None)
    brand = params.get('brand', None)
    model = params.get('model', None)

    filters = {}

    if country_code:
        filters['country_code'] = country_code
    if model:
        filters['model'] = model
    if brand:
        filters['brand'] = brand

    if feedback_subcategory:
        filters['feedback_subcategory'] = feedback_subcategory

    queryset = CustomerFeedback.objects.filter(**filters)

    # annotation functions for sentiment counts
    positive = Count('id', filter=Q(feedback_sentiment='Positive'))
    neutral = Count('id', filter=Q(feedback_sentiment='Neutral'))
    negative = Count('id', filter=Q(feedback_sentiment='Negative'))

    # group responses by date
    if group_by == 'day':
        feedback_by_day = queryset.values('post_date')
        sentiments = (
            feedback_by_day
            .annotate(positive=positive)
            .annotate(neutral=neutral)
            .annotate(negative=negative)
            .order_by('post_date')
        )

    # group responses by month (e.g. to increase sample size)
    elif group_by == 'month':
        feedback_by_month = queryset.annotate(
            month=TruncMonth('post_date')
        ).values('month')
        sentiments = (
            feedback_by_month
            .annotate(positive=positive)
            .annotate(neutral=neutral)
            .annotate(negative=negative)
            .order_by('month')
        )

    # group responses by year (e.g. for summary view)
    elif group_by == 'year':
        feedback_by_year = queryset.annotate(
            year=TruncYear('post_date')
        ).values('year')
        sentiments = (
            feedback_by_year
            .annotate(positive=positive)
            .annotate(neutral=neutral)
            .annotate(negative=negative)
            .order_by('year')
        )

    if group_by is not None:
        serializer = CustomerFeedbackAnnotatedSerializer(sentiments, many=True)
    else:
        serializer = CustomerFeedbackSerializer(queryset, many=True)

    return JsonResponse(serializer.data, safe=False)
