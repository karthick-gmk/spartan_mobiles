from typing import Any
from django.core.management.base import BaseCommand
from spartans.models import Service, Servicetype

class Command(BaseCommand):
    help = "Service data for the spartans app"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data
        Servicetype.objects.all().delete()

        # Create Service instances
        software_service, _ = Service.objects.get_or_create(name='Software & OS Issues')
        motherboard_service, _ = Service.objects.get_or_create(name='Motherboard Service')
        display_service, _ = Service.objects.get_or_create(name='Mobile Display Replacement')

        servicetype_data = [
            {
                'service': software_service,
                'discription': 'We solve software problems like hanging, booting issue, OS installation, data recovery & performance tuning.',
                'text': ' ',
                'service_type': 'Fast Support',
                'image_url': 'https://www.validity.com/wp-content/uploads/2023/08/AdobeStock_580585296-scaled.jpeg'
            },
            {
                'service': motherboard_service,
                'discription': 'We fix all types of motherboard issues such as dead phone, no power, charging problems, network issues, and more.',
                'text': ' ',
                'service_type': 'Expert Repair',
                'image_url': 'https://t4.ftcdn.net/jpg/08/18/89/55/240_F_818895529_Qb0kmWgnz2ZLfMSJpFVvOouyBC8evwQd.jpg'
            },
            {
                'service': display_service,
                'discription': 'We provide high-quality original & compatible display replacements for all mobile brands with fast and reliable service.',
                'text': '" FREE " Mobile Pouch  , Headphone , Temper Glass  , Mobile Stand',
                'service_type': 'Quick Service',
                'image_url': 'https://t3.ftcdn.net/jpg/05/19/73/36/240_F_519733648_tSMSHwqxw3TrbgFSXNKJVKncdkC0siTq.jpg'
            },
        ]

        for data in servicetype_data:
            Servicetype.objects.create(**data)

        self.stdout.write(
            self.style.SUCCESS('Successfully created service types')
        )
