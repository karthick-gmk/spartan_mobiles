from django.db import models
from usermanagement.models.user_model import User
from spartans.models.product_model import product as Product
import uuid
from django.utils import timezone

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    )

    order_number = models.CharField(max_length=20, unique=True, blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.order_number:
            date_str = timezone.now().strftime('%Y%m%d')
            self.order_number = f"SM{date_str}{uuid.uuid4().hex[:6].upper()}"
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Order {self.order_number} - {self.user.username}"

    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="order_items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return self.product.name





class OrderTracking(models.Model):

    TRACKING_STATUS = (
        ('shipped', 'Shipped'),
        ('courier', 'Moved to Courier'),
        ('reached_city', 'Reached City'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
    )

    order = models.OneToOneField(Order,related_name='tracking',on_delete=models.CASCADE)
    status = models.CharField(max_length=100,choices=TRACKING_STATUS,default='shipped')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.order.id} - {self.get_status_display()}"
    
