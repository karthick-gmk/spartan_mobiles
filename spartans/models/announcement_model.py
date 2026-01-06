from django.db import models
from django.utils import timezone
from .product_model import product


class Announcement(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE, null=True, blank=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'announcement'
    
    def __str__(self):
        return self.product.name if self.product else "No Product"
    
    def time_remaining(self):
            now = timezone.now()
            if self.end_time > now:
                diff = self.end_time - now
                return {
                    "days": diff.days,
                    "hours": diff.seconds // 3600,
                    "minutes": (diff.seconds % 3600) // 60,
                    "seconds": diff.seconds % 60,
                }
            return {"days": 0, "hours": 0, "minutes": 0, "seconds": 0}