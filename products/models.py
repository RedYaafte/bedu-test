from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.FloatField()
    stock = models.PositiveIntegerField()
    tags = models.ManyToManyField('Tag')
    categories = models.ForeignKey(
        'Category', on_delete=models.CASCADE, null=True)


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(MPTTModel):
    name = models.CharField(max_length=150)
    products = TreeForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']
