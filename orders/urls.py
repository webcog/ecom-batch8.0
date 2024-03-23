from django.urls import path
from orders.views import checkout
urlpatterns = [
    path('checkout/', checkout, name='checkout'),
]
