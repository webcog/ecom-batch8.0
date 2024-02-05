from django.db import models
from category.models import Category
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=255,unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    # product_image = models.ImageField()
    # PILLOW 
    # media setup
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)