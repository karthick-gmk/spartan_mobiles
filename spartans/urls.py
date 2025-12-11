from django.urls import path
from . import views


app_name = 'spartans'

urlpatterns = [
    path("", views.index, name='index'),
    path('detail/<int:product_id>/<str:product_name>/', views.detail, name='detail'),
    path("contact", views.contact, name='contact'),
    path("about", views.about, name='about'),
    path('shop', views.shop, name='shop'),
    path('service_type',views.service_type,name='service-type'),
    path('checkout', views.checkout, name='checkout'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in',views.sign_in, name='sign_in'),
    path('logout',views.logout,name='logout'),
    path('forget', views.forget, name='forget'),
    path('reset_pw', views.reset_pw, name='reset_pw'),
    path('shoping_card', views.shoping_card, name='shoping_card'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    
    ]

