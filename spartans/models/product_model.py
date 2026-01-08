from django.db import models
from .master_model import Brand, BrandModel, Category
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from .master_model import Category, Brand, BrandModel



def product_main_image_path(instance, filename):
    product = slugify(instance.name)
    brand = slugify(instance.brand.name)
    return f"products/{brand}/{product}/main_image/{filename}"

class product(models.Model):
    name = models.CharField(max_length=1000)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    brand_model = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    main_image = models.ImageField(upload_to=product_main_image_path, help_text="Main display image", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    specifications = models.TextField(null=True, blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
    is_new = models.BooleanField(default=False, help_text="Mark as New Arrival")
    on_sale = models.BooleanField(default=False, help_text="Mark as Hot Deal/Sale")
    is_best_seller = models.BooleanField(default=False, help_text="Mark as Best Seller")
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

    def get_gallery_images(self):
        return self.productimage_set.all()


def product_image_path(instance, filename):
        brand = slugify(instance.product.brand.name)
        product = slugify(instance.product.name)
        return f"products/{brand}/{product}/images/{filename}"



class ProductImage(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_image_path)

    class Meta:
        db_table = 'product_image'
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return f"{self.product.name} - Image {self.id}"
    


