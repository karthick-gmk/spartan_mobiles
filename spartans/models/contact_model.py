from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    message = models.TextField()


    class Meta:
        db_table = 'contact'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


    def __str__(self):
        return self.name