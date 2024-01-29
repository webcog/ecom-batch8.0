from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Categories"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name
    

class Wajahat(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Wajahat Murtaza"
        verbose_name_plural = "Wajahat Murtaza"
