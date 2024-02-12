from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    cat_img = models.ImageField(upload_to="cat_img/", null=True, blank=True)
    

    class Meta:
        verbose_name = "Categories"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name
    
