from rest_framework import serializers

from feedback.models import CustomerFeedback


class CustomerFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerFeedback
        fields = [
            'customer_id',
            'post_date',
            'country_code',
            'brand',
            'model',
            'ownership_status',
            'feedback_sentiment',
            'feedback_subcategory',
        ]


class CustomerFeedbackAnnotatedSerializer(serializers.ModelSerializer):
    positive = serializers.IntegerField()
    neutral = serializers.IntegerField()
    negative = serializers.IntegerField()
    month = serializers.DateField(required=False)
    year = serializers.DateField(required=False)

    class Meta:
        model = CustomerFeedback
        fields = (
            'post_date',
            'month',
            'year',
            'positive',
            'neutral',
            'negative'
        )
