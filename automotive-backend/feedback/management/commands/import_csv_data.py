from collections import namedtuple
from datetime import datetime

from django.core.management.base import BaseCommand

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
    with open('interview-data.csv') as f:
        data = f.readlines()

    for index, line in enumerate(data[1:]):
        try:
            row = parse_line(line)
            save_row_to_db(row)
        except Exception as e:
            print(f'Error at row {index + 2}')
            print(e)
            print(line)
            # sys.exit(1)


def parse_line(line):
    row = [cell.strip() for cell in line.split(',')]
    row_tuple = Feedback(*row)
    return row_tuple


def save_row_to_db(row):
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
        serializer.save()
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
