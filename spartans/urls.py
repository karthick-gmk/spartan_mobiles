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
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in',views.sign_in, name='sign_in'),
    path('forget', views.forget, name='forget'),
    path('logout',views.logout,name='logout'),
    path('reset_pw/<uidb64>/<token>', views.reset_pw, name='reset_pw'),

    ]


