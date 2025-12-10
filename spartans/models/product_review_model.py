from django.db import models
from usermanagement.models.user_model import User
from .product_model import product

class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_review'
        unique_together = ('user', 'product')  # One review per user per product
    

    def __str__(self):
        return f"{self.user.first_name} - {self.product.name}"