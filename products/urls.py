from django.urls import path
from products.views import index, shop, detail

urlpatterns = [
   path("", index, name="index"),
   path("shop/", shop, name="shop"),
   path("product/<str:slug>", detail, name="detail"),
]
