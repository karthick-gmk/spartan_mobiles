from typing import Any
from spartans.models import Service
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Populate services data for the spartans app"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data
        Service.objects.all().delete()

        services_data = [
            {
                'title': 'Mobile Display Replacement',
                'service_type': 'Quick Service',
                'description': 'We provide high-quality original & compatible display replacements for all mobile brands with fast and reliable service.',
                'image_url': 'https://images.unsplash.com/photo-1556656793-08538906a9f8?w=500&auto=format&fit=crop&q=60',
                'order': 1
            },
            {
                'title': 'Motherboard Service',
                'service_type': 'Expert Repair',
                'description': 'We fix all types of motherboard issues such as dead phone, no power, charging problems, network issues, and more.',
                'image_url': 'https://plus.unsplash.com/premium_photo-1681426669771-d2113672a49b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8bW90aGVyYm9hcmR8ZW58MHx8MHx8fDA%3D',
                'order': 2
            },
            {
                'title': 'Software & OS Issues',
                'service_type': 'Fast Support',
                'description': 'We solve software problems like hanging, booting issue, OS installation, data recovery & performance tuning.',
                'image_url': 'https://images.unsplash.com/photo-1607799279861-4dd421887fb3?w=500&auto=format&fit=crop&q=60',
                'order': 3
            }
        ]

        for data in services_data:
            Service.objects.create(**data)
            
        self.stdout.write(self.style.SUCCESS('Successfully created services'))
