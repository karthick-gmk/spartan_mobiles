from typing import Any
from django.core.management.base import BaseCommand
from spartans.models import Service

class Command(BaseCommand):
    help = "Service data for the spartans app"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data
        Service.objects.all().delete()

        service_data = [
            {'name': 'Mobile Display Replacement'},
            {'name': 'Motherboard Service'},
            {'name': 'Software & OS Issues'},
            {'name': 'Other'},
        ]

        for data in service_data:
            Service.objects.create(**data)

        self.stdout.write(
            self.style.SUCCESS('Successfully created services')
        )
