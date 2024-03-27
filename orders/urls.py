from django.urls import path
from orders.views import checkout, order_detail
urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('order_detail/<int:order_id>', order_detail, name='order_detail'),
]
