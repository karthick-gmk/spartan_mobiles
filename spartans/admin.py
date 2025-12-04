from django.contrib import admin
from .models import product, Service, Brand, BrandModel, Category
from .models.product_model import ProductImage

admin.site.register(product)
admin.site.register(Service)
admin.site.register(Brand)
admin.site.register(BrandModel)
admin.site.register(Category)
admin.site.register(ProductImage)
