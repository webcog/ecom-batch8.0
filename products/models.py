from django.db import models
from category.models import Category
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=255,unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    product_image = models.ImageField(upload_to='product/')
    product_image_two = models.ImageField(upload_to='product/')
    product_image_three = models.ImageField(upload_to='product/')
    product_image_four = models.ImageField(upload_to='product/')
    # PILLOW 
    # media setup
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.product_name
    
