import sys
from collections import namedtuple
from datetime import datetime

from django.core.management.base import BaseCommand

from feedback.models import CustomerFeedback
from feedback.serializers import CustomerFeedbackSerializer


Feedback = namedtuple(
    'Feedback',
    [
        'customer_id',
        'post_date',
        'reporting_date',
        'country_code',
        'author_id',
        'overall_sentiment',
        'brand',
        'model',
        'variant',
        'ownership_status',
        'vehicle_id',
        'id_3',
        'feedback_sentiment',
        'feedback_subcategory',
    ]
)


def import_data():
    try:
        with open('interview-data.csv') as f:
            data = f.readlines()
    except FileNotFoundError:
        print(
            "ERROR: 'interview-data.csv' not found. This file needs to be copied into "
            "the 'automotive-backend' directory before building the Docker container."
        )
        sys.exit(1)

    # crude idempotency check - for rough setup only
    database_count = CustomerFeedback.objects.count()
    if database_count > 9000:
        print("Database has already been populated; skipping database import.")
        sys.exit(0)

    feedback_items = []

    for index, line in enumerate(data[1:]):
        try:
            row = parse_line(line)
            valid_data = parse_row_data(row)
            if valid_data:
                feedback_items.append(CustomerFeedback(**valid_data))
        except Exception as e:
            print(f'Error at row {index + 2}')
            print(e)
            print(line)

    if feedback_items:
        CustomerFeedback.objects.bulk_create(feedback_items)


def parse_line(line):
    row = [cell.strip() for cell in line.split(',')]
    row_tuple = Feedback(*row)
    return row_tuple


def parse_row_data(row):
    data = {
        'customer_id': int(row.customer_id),
        'post_date': format_date(row.post_date),
        'country_code': row.country_code,
        'overall_sentiment': row.overall_sentiment,
        'brand': row.brand,
        'model': row.model,
        'ownership_status': row.ownership_status,
        'feedback_sentiment': row.feedback_sentiment,
        'feedback_subcategory': row.feedback_subcategory,
    }

    serializer = CustomerFeedbackSerializer(data=data)

    if serializer.is_valid():
        return serializer.validated_data
    else:
        print(serializer.errors)


def format_date(d: str):  # e.g. 17/03/2025
    date = datetime.strptime(d, '%d/%m/%Y')
    print(date)
    return f"{date:%Y-%m-%d}"


class Command(BaseCommand):
    help = 'Imports CSV feedback data'

    def handle(self, *args, **options):
        print('Importing data...')
        import_data()

        self.stdout.write(self.style.SUCCESS('Import is complete.'))
