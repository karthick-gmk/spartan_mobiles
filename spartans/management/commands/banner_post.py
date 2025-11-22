from typing import Any
from spartans.models import Banner
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Banner data for the spartans app"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data
        Banner.objects.all().delete()
        
        banners_data = [
            {
                'title': 'Mobile Repair Services',
                'banner_type': 'repair',
                'image_url': 'https://t3.ftcdn.net/jpg/02/40/25/00/240_F_240250083_uv4BiZdDXnE11RxoDm3DoLEaAEs0X28H.jpg',
                'link_text': 'Book Now',
                'order': 1
            },
            {
                'title': 'Mobile Accessories',
                'banner_type': 'accessories',
                'image_url': 'https://t3.ftcdn.net/jpg/01/89/82/26/240_F_189822641_jMRbE9jVlBtSWqtDQ0bxfFFOWpKlJxjs.jpg',
                'link_text': 'Shop Accessories',
                'order': 2
            },
            {
                'title': 'Latest Smartphones & Gadgets',
                'banner_type': 'smartphones',
                'image_url': 'https://images.unsplash.com/photo-1557906757-fbb05fc2fcee?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fExhdGVzdCUyMFNtYXJ0cGhvbmVzJTIwJTI2JTIwR2FkZ2V0c3xlbnwwfHwwfHx8MA%3D%3D',
                'link_text': 'View Products',
                'order': 3
            },
        ]

        for banner_data in banners_data:
            Banner.objects.create(**banner_data)
            
        self.stdout.write(self.style.SUCCESS('Successfully created banners'))
