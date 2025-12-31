from django.db import models
from .master_model import Brand, Category, BrandModel
from usermanagement.models.user_model import User

class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        db_table = 'service'
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name    



class Servicetype(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    discription = models.TextField()
    text = models.TextField(null=True, blank=True)
    service_type = models.CharField(max_length=100)
    image_url = models.URLField(null=True, blank=True)
   
    class Meta:
        db_table = 'servicetype'
        verbose_name = 'Servicetype'
        verbose_name_plural = 'Servicetypes'

    def __str__(self):
        return f"{self.service.name} - {self.service_type}"



    


class UserRequestService(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    brandModel = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending') # Enum need to add 


    class Meta:
        db_table = 'user_request_service'
        verbose_name = 'User Request Service'
        verbose_name_plural = 'User Request Services'

    def __str__(self):
        return f"{self.user.username} - {self.service.name}"