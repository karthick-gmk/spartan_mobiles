from django.core.management.base import BaseCommand
from spartans.models import Shop as ShopModel

class Command(BaseCommand):
    def handle(self, *args, **options):
        products = [
            {"name": "Fast Charging USB Cable", 
             "price": 299, 
             "image_url":"https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8bW9iaWxlJTIwY2hhcmdlcnxlbnwwfHwwfHx8MA%3D%3D", 
             "category": "memory-card",
             "brand": "samsung", 
             "rating": 3
             },
            {"name": "Bluetooth Earbuds",
             "price": 1499, 
            "image_url": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZWFyYnVkc3xlbnwwfHwwfHx8MA%3D%3D", 
            "category": "chargers",   
            "brand": "apple", 
            "rating": 4,
             "is_sale": True
             },
            {"name": "Mobile Back Cover", 
            "price": 199, 
            "image_url": "https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8bW9iaWxlfGVufDB8fDB8fHww", 
            "category": "earphones",       
            "brand": "xiaomi", 
            "rating": 2
            },
            {"name": "Smartwatch",
             "price": 2999, 
            "image_url": "https://images.unsplash.com/photo-1660844817855-3ecc7ef21f12?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c21hcnR3YXRjaHxlbnwwfHwwfHx8MA%3D%3D",
             "category": "power-banks" , 
            "brand": "apple", 
            "rating": 4,
             "is_sale": True
             },
            {"name": "Tempered Glass Protector",
             "price": 149,
             "image_url": "https://images.unsplash.com/photo-1634403665481-74948d815f03?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fG1vYmlsZXxlbnwwfHwwfHx8MA%3D%3D",
             "category": "screen-guards", 
            "brand": "oneplus",
             "rating": 3
             },
            {"name": "Portable Mobile Stand", 
            "price": 249, 
            "image_url": "https://images.unsplash.com/photo-1760443728230-b84a87381f8f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8UG9ydGFibGUlMjBNb2JpbGUlMjBTdGFuZHxlbnwwfHwwfHx8MA%3D%3D",
           "category": "smartwatches" ,  
            "brand": "realme", 
            "rating": 2
            },
        ]
        
        ShopModel.objects.all().delete()
        
        for product_data in products:
            ShopModel.objects.create(**product_data)
        
        self.stdout.write("Shop products created successfully")
