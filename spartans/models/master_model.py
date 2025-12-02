from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

# Create your models here.
class Brand(models.Model):

    name = models.CharField(max_length=100, unique=True)
    category = models.ManyToManyField(Category, related_name='brands', blank=True)


    # CASCADE,
    # DO_NOTHING,
    # PROTECT,
    # RESTRICT,
    # SET,
    # SET_DEFAULT,
    # SET_NULL,
    

    class Meta:
        db_table = 'brand'
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


    def __str__(self):
        return self.name


class BrandModel(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        db_table = 'brand_model'
        verbose_name = 'Brand Model'
        verbose_name_plural = 'Brand Models'

    def __str__(self):
        return self.name




