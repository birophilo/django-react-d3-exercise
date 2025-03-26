from django.db import models


SENTIMENT_CHOICES = [
    ('Positive', 'Positive'),
    ('Neutral', 'Neutral'),
    ('Negative', 'Negative'),
]

OWNERSHIP_CHOICES = [
    ('Owner', 'Owner'),
    ('Pre-Ownership', 'Pre-Ownership'),
    ('Showing Interest', 'Showing Interest'),
    ('Not an Owner', 'Not an Owner'),
    ('UNSURE', 'UNSURE'),
]

FEEDBACK_SUBCATEGORIES = [
    # ordered by popularity in the dataset, descending order
    'Product Concern/Query',
    'Overall Satisfaction With the Car',
    'Quality',
    'Autonomy/Range',
    'Charging Experience',
    'Test Drive',
    'Overall Disappointment with the Brand',
    'Handling/Driving Experience',
    'Exterior Design',
    'Equipment/Specifications',
    'Price',
    'Interior Design',
    'Battery',
    'Switching to Another Brand',
    'Order Status',
    'Driving Technologies',
    'Delivery Timings',
    'Infotainment',
    'Charging Infrastructure',
    'OTA Update',
    'OEM Apps',
    'Resale Value',
    'Brand/Product Pride',
    'Aftersales (Dealer)',
    'Overall Disappointment With the Brand',
    'Communication From Brand',
    'Range',
    'Customer Care',
    'Safety & Security',
    '12V Battery',
    'Electric Driving Experience',
    'Switching to Another Vehicle',
    'Overall Satisfaction with the Brand',
    'Accessories',
    'Satisfaction With Handover',
    'Tyres',
    'Communication With Dealer',
    'PAAK',
    'Driving Modes Experience',
    'Connectivity (OEM Apps)',
    'Cancellation',
    'Servicing',
    'Owners Manual',
    'Ordering Process',
    'Aftersales (OEM App Support)',
    'Communication from Brand',
    'Satisfaction with Handover',
    'Recall',
    'Communication with Dealer',
    'Connectivity',
    'Overall Satisfaction with the Car',
    'OEM App Support Team',
    'Towing Experience',
    'Handling/Driving experience',
    'Specific OEM Apps',
    'OEM Charge Network Solution',
    'Charging experience',
    'Brand Strategy/Portfolio',
    'Switching to another brand',
    'Switching to Another Car',
    'Overall satisfaction With the Car',
    'Orderring Process',
    'Order status',
    'OEM app support team',
    'OEM Charge Network Solution (BlueOval Charge Network etc)',
    'Leasing Companies',
    'Driving technologies',
    'Communication from Dealer',
]


class CustomerFeedback(models.Model):
    customer_id = models.IntegerField()
    post_date = models.DateField(blank=True)
    country_code = models.CharField(max_length=255)
    overall_sentiment = models.CharField(max_length=255, choices=SENTIMENT_CHOICES)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    ownership_status = models.CharField(max_length=255, choices=OWNERSHIP_CHOICES)
    feedback_sentiment = models.CharField(max_length=255)
    feedback_subcategory = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.post_date}: {self.customer_id} ({self.country_code}) {self.model} {self.feedback_sentiment}"
