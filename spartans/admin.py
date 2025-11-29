from django.contrib import admin
from .models import product, Service, Brand, BrandModel, Category

admin.site.register(product)
admin.site.register(Service)
admin.site.register(Brand)
admin.site.register(BrandModel)
admin.site.register(Category)
