from django.db import models
from django.contrib.auth.models import User 
from products.models import Product
# Create your models here.
class Order(models.Model):
    STATUS = (
        ("New","New"),
        ("Accepted","Accepted"),
        ("On the Way","On the Way"),
        ("Completed","Completed"),
        ("Cancelled","Cancelled"),
    )

    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    order_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    addres_line_1 = models.CharField(max_length=255)
    addres_line_2 = models.CharField(max_length=255)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=5)
    order_note = models.TextField(blank=True, null=True)
    order_total = models.FloatField()
    tax = models.FloatField()
    shipping_charges = models.FloatField()
    is_order = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS, default="New")

    def __str__(self):
        return self.first_name
    

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_price = models.FloatField()
    quantity = models.IntegerField()
    ordered = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product.product_name