from django.core.management.base import BaseCommand
from spartans.models import Instagram

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Create Instagram instance
        instagram, created = Instagram.objects.get_or_create(
            defaults={
                'title': 'Instagram',
                'description': 'Explore the latest mobile accessories — headphones, chargers, speakers, memory cards, and more. Follow us for daily tech updates and offers.',
                'hashtag': '#Electronic_Store',
                'is_active': True
            }
        )
        
       
        self.stdout.write("Instagram data created successfully")
