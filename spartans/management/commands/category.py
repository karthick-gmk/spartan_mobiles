from typing import Any
from django.core.management.base import BaseCommand
from spartans.models import Category

class Command(BaseCommand):
    help = "category data for the spartans app"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data
        Category.objects.all().delete()

        category_data = [
            {'name': 'Mobile'},
            {'name': 'Headphone'},
            {'name': 'Bluetooth Headphone'},
            {'name': 'Bluetooth Speaker'},
            {'name': 'Charger'},
            {'name': 'Memory Card'},
        ]

        for data in category_data:
            Category.objects.create(**data)

        self.stdout.write(
            self.style.SUCCESS('Successfully created categories')
        )
