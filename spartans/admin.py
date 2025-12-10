from django.contrib import admin
from .models import product, Service, Brand, BrandModel, Category
from .models.product_model import ProductImage
from .models.service_model import UserRequestService
from .models.product_review_model import ProductReview
from .models.contact_model import Contact

admin.site.register(product)
admin.site.register(Service)
admin.site.register(Brand)
admin.site.register(BrandModel)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(UserRequestService)
admin.site.register(ProductReview)
admin.site.register(Contact)