from typing import Any
from spartans.models import Category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "category data for the spartans app"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data
        Category.objects.all().delete()

        category_data = [
            {
                'name': 'Mobile Accessories',
                'description': 'Gadgets & Devices',
                'items': 'Headphones, Tempered Glass, Speakers, Bluetooth Headphones, Pen Drive, Charger, Memory Card, Airbuds'
            }
        ]

        for data in category_data:
            Category.objects.create(**data)
            
        self.stdout.write(self.style.SUCCESS('Successfully created categories'))
