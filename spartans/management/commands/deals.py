from typing import Any
from spartans.models import Deal
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = " deals data for the spartans app"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data
        Deal.objects.all().delete()

        deals_data = [
            {
                'title': 'Deal Of The Week',
                'product_name': 'Wireless Bluetooth Headphones',
                'sale_price': 499.00,
                'image_url': 'https://plus.unsplash.com/premium_photo-1678099940967-73fe30680949?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8aGVhZHBob25lc3xlbnwwfHwwfHx8MA%3D%3D',
                'days': 3,
                'hours': 1,
                'minutes': 50,
                'seconds': 18
            }
        ]

        for data in deals_data:
            Deal.objects.create(**data)
            
        self.stdout.write(self.style.SUCCESS('Successfully created deals'))
