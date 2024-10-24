import csv
import os
from slugify import slugify
from phones.models import Phone
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    def handle(self, *args, **options):
        path = os.path.abspath('phones.csv')
    
       
        with open(path, newline='') as f:
            csv_dict = csv.DictReader(f, delimiter=';')
          
            for i in csv_dict:
                a = slugify(i['name'])
                b = Phone(
                    id = i['id'],
                    name = i['name'],
                    price = i['price'],
                    image = i['image'],
                    release_date = i['release_date'],
                    lte_exists = i['lte_exists'],
                    slug = a
                )
                print(a)
                print(b)
                b.save()

        
        