from django.urls import path
from cart.views import add_to_cart


urlpatterns = [
    path("add-to-cart/<slug:product_slug>", add_to_cart, name="add_to_cart"),
]
