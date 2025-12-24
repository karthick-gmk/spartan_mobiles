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
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in',views.sign_in, name='sign_in'),
    path('logout',views.logout,name='logout'),
    path('forget', views.forget, name='forget'),
    path('reset_pw', views.reset_pw, name='reset_pw'),
    path('shoping_card', views.shoping_card, name='shoping_card'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_cart/<int:cart_id>/', views.remove_cart, name='remove_cart'),
    path('add_to_favorite/<int:product_id>/', views.add_to_favorite, name='add_to_favorite'),
    path('favorites', views.favorites, name='favorites'),
    path('remove_favorite/<int:favorite_id>/', views.remove_favorite, name='remove_favorite'),
    path('update_cart_quantity/', views.update_cart_quantity, name='update_cart_quantity'),
    path('delete_address/', views.delete_address, name='delete_address'),

    ]

