from django.contrib import admin
from .models import product, Service, Brand, BrandModel


@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'brand_model', 'price', 'rating']
    list_filter = ['brand', 'brand_model']
    search_fields = ['name', 'brand__name', 'brand_model__name']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'service_type', 'category']
    list_filter = ['service_type', 'category']
    search_fields = ['name', 'discription']

