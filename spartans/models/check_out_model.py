from django.db import models


class Checkout(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=20)


    class Meta:
        db_table = 'checkout'
        verbose_name = 'checkout'
        verbose_name_plural = 'checkouts'

    def __str__(self):
        return self.name

