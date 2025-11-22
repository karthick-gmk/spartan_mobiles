from django.urls import path
from . import views

app_name = 'spartans'

urlpatterns = [
    path("", views.index, name='index'),
    path("detail", views.detail, name='detail'),
    path("contact", views.contact, name='contact'),
    path("about", views.about, name='about'),
    path('shop', views.shop, name='shop'),
    path('shoping', views.shoping, name='shoping'),
    path('checkout', views.checkout, name='checkout'),
    ]


