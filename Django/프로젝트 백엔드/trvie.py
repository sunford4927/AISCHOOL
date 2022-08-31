import csv
import os
import django
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()
from users.models import *
with open('foodend.csv') as csv_file:
    rows = csv.reader(csv_file)
    next(rows, None)
    for row in rows:
        # is_verified = json.loads(row[0].lower())
        foodends.objects.create(
            foodname = row[0],
            price = row[1],
            score = str(row[2]),
            location = row[3],
            name = row[4],
            category = row[5]
        )
        print(row)













