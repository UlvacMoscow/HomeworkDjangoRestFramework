from django import forms
from .models import Customer, Order, Product


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'mail']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'customer', 'order']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name']


