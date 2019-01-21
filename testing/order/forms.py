from django import forms
from customer.models import Customer
from .models import Order



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email',]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'customer']






