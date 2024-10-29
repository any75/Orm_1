import csv
import os
from datetime import datetime 
from phones.models import Phone
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    def handle(self, *args, **options):
        path = os.path.abspath('phones.csv')
    
       
        with open(path, newline='') as f:
            csv_dict = csv.DictReader(f, delimiter=';')
          
            for i in csv_dict:
             
                b = Phone(
                    id = i['id'],
                    name = i['name'],
                    price = round(float(i['price']), 2),
                    image = i['image'],
                    release_date = datetime.strptime(i['release_date'], "%Y-%m-%d").date(),
                    lte_exists = i['lte_exists'] == "True"
                    
                )
           
                b.save()

        
        
        
        
