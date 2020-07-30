import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wisely.settings")
django.setup()

from orders.models import Review, OrderItem, Order, OrderImage, OrderStatus

CSV_PATH_REVIEW = '../wisely_review.csv'

with open(CSV_PATH_REVIEW) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        rate_c = row[1]
        review_text_c = row[2]
        Review.objects.create(rate = rate_c, review_text=row[2])





