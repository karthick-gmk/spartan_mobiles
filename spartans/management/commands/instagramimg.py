from django.core.management.base import BaseCommand
from spartans.models import InstagramImage

class Command(BaseCommand):
    def handle(self, *args, **options):
        images = [
                    "https://plus.unsplash.com/premium_photo-1678099940967-73fe30680949?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8aGVhZHBob25lc3xlbnwwfHwwfHx8MA%3D%3D",
                    "https://plus.unsplash.com/premium_photo-1670462145713-b79606affb0b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8bW9iaWxlJTIwYWNjZXNzb3JpZXN8ZW58MHx8MHx8fDA%3D", 
                    "https://images.unsplash.com/photo-1623998022290-a74f8cc36563?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fG1vYmlsZSUyMGFjY2Vzc29yaWVzfGVufDB8fDB8fHww",
                    "https://images.unsplash.com/photo-1598382143506-2ac06c28d203?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fG1vYmlsZSUyMGFjY2Vzc29yaWVzfGVufDB8fDB8fHww",
                    "https://images.unsplash.com/photo-1753385158278-387d4dda60c4?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjh8fG1vYmlsZSUyMGFjY2Vzc29yaWVzfGVufDB8fDB8fHww",
                    "https://images.unsplash.com/photo-1758578070291-0c22ff555df9?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzF8fG1vYmlsZSUyMGFjY2Vzc29yaWVzfGVufDB8fDB8fHww"
                ]
                
        InstagramImage.objects.all().delete()
        
        for i, img in enumerate(images):
            InstagramImage.objects.create(
                image_url=img,
                order=i,
                is_active=True
            )
        self.stdout.write("Instagram data created successfully")