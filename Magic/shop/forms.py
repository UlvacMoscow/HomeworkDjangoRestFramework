from django import forms
from .models import Customer, Order, Products


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'customer', 'product']


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['Category', 'name', 'metal', 'stone']