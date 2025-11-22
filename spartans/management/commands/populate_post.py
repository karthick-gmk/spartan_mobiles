from typing import Any
from spartans.models import Product
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Populate data for the spartans app"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data
        Product.objects.all().delete()

        products_data = [
            {
                "name": "Bluetooth Headphones",
                "price": 799.00,
                "category": "new-arrivals",
                "rating": 4.5,
                "is_new": True,
                "is_sale": False,
                "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=300"
            },
            {
                "name": "Fast Mobile Charger", 
                "price": 499.00,
                "category": "hot-sales",
                "rating": 4.0,
                "is_new": False,
                "is_sale": True,
                "image_url": "https://images.unsplash.com/photo-1583394838336-acd977736f90?w=300"
            },
            {
                "name": "Premium Tempered Glass",
                "price": 99.00,
                "category": "new-arrivals", 
                "rating": 4.2,
                "is_new": False,
                "is_sale": True,
                "image_url": "https://images.unsplash.com/photo-1512499617640-c74ae3a79d37?w=300"
            },
            {
                "name": "Bluetooth Speaker",
                "price": 1299.00,
                "category": "hot-sales", 
                "rating": 4.8,
                "is_new": True,
                "is_sale": False,
                "image_url": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=300"
            },
            {
                "name": "Bluetooth Headphones",
                "price": 799.00,
                "category": "new-arrivals",
                "rating": 4.5,
                "is_new": True,
                "is_sale": False,
                "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=300"
            },
            {
                "name": "Fast Mobile Charger", 
                "price": 499.00,
                "category": "hot-sales",
                "rating": 4.0,
                "is_new": False,
                "is_sale": True,
                "image_url": "https://images.unsplash.com/photo-1583394838336-acd977736f90?w=300"
            },
            {
                "name": "Premium Tempered Glass",
                "price": 99.00,
                "category": "new-arrivals", 
                "rating": 4.2,
                "is_new": False,
                "is_sale": True,
                "image_url": "https://images.unsplash.com/photo-1512499617640-c74ae3a79d37?w=300"
            },
            {
                "name": "Bluetooth Speaker",
                "price": 1299.00,
                "category": "hot-sales", 
                "rating": 4.8,
                "is_new": True,
                "is_sale": False,
                "image_url": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=300"
            }
        ]

        for data in products_data:
            Product.objects.create(**data)
            
        self.stdout.write(self.style.SUCCESS('Successfully populated products'))
