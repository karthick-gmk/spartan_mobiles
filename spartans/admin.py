from django.contrib import admin
from .models import product, Service, Brand, BrandModel, Category
from .models.product_model import ProductImage
from .models.service_model import UserRequestService
from .models.product_review_model import ProductReview
from .models.contact_model import Contact
from .models.shop_cart import Cart 
from .models.billing_model import BillingAddress,UserAddress
from .models.order_model import Order, OrderItem
from .models.shop_cart import CartItem
from .models.shop_cart import Favorite
from .models.service_model import UserRequestService, Servicetype
from .models.announcement_model import Announcement

admin.site.register(product)
admin.site.register(Service)
admin.site.register(Brand)
admin.site.register(BrandModel)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(UserRequestService)
admin.site.register(ProductReview)
admin.site.register(Contact)
admin.site.register(Cart)
admin.site.register(Favorite)
admin.site.register(BillingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(CartItem)
admin.site.register(UserAddress)
admin.site.register(Servicetype)
admin.site.register(Announcement)

