from django.db import models
from .master_model import Brand, BrandModel, Category
from django.core.validators import MinValueValidator, MaxValueValidator




class product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    brand_model = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(null=True, blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],null=True,blank=True)

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def __str__(self):
        return self.name


    def get_price_range(self):
        price = float(self.price)
        if price <= 100:
            return "0-100"
        elif price <= 200:
            return "100-200"
        elif price <= 300:
            return "200-300"
        elif price <= 400:
            return "300-400"
        else:
            return "500-plus"



      