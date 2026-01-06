from typing import Any
from django.core.management.base import BaseCommand
from spartans.models import Brand

class Command(BaseCommand):
    help = "barnd data for the spartans app"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data
        Brand.objects.all().delete()

        brand_data = [
            {'name': 'Apple'},
            {'name': 'Vivo'},
            {'name': 'Oppo'},
            {'name': 'Realme'},
            {'name': 'Redmi'},
            {'name': 'iqoo'},
        ]

        for data in brand_data:
            Brand.objects.create(**data)

        self.stdout.write(
            self.style.SUCCESS('Successfully created brand')
        )
