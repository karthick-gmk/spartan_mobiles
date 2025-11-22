from django.shortcuts import render
from .models import Product
from .models import Product, Banner, Category, Deal, Service, Instagram, InstagramImage,Shop

def index(request):
    products = Product.objects.all()
    banners = Banner.objects.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)
    deals = Deal.objects.filter(is_active=True).first()
    services = Service.objects.filter(is_active=True)
    instagram = Instagram.objects.filter(is_active=True).first()
    instagram_images = InstagramImage.objects.filter(is_active=True)
    return render(request, 'index.html', {
        'products': products, 
        'banners': banners,
        'categories': categories,
        'deal': deals,
        'services': services,
        'instagram': instagram,
        'instagram_images': instagram_images
    })






def shop(request):
    shop_products = Shop.objects.filter(is_active=True)
    return render(request, 'shop.html', {'shop_products': shop_products})



def detail(request):
    return render(request, 'detail.html')


def about(request):
    return render(request, 'about.html')



def contact(request):
    return render(request, 'contact.html')

def shoping(request):
    return render(request, 'shoping-card.html')

def checkout(request):
    return render(request, 'checkout.html')