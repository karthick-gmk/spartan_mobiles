from django.contrib import admin
from .models import Product, Banner
# Register your models here.
# admin.py

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'rating']
    list_filter = ['category', 'is_new', 'is_sale']

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'banner_type', 'is_active', 'order']
    list_filter = ['banner_type', 'is_active']
    ordering = ['order']
