from django import forms
from orders.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'addres_line_1', 'addres_line_2', 'country', 'state', 'city', 'postal_code', 'order_note']