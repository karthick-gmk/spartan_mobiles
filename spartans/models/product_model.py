from django.db import models
from .master_model import Brand, BrandModel, Category



class product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    brand_model = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def __str__(self):
        return self.name



    




      