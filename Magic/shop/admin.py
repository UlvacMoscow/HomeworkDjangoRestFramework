from django.contrib import admin
from django import forms
from .models import Customer, Order, Products

class CustomerAdminForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'


class CustomerAdmin(admin.ModelAdmin):
    form = CustomerAdminForm
    list_display = ['name', 'email', 'phone']
    readonly_fields = ['name', 'email', 'phone']

admin.site.register(Customer, CustomerAdmin)


class OrderAdminForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'


class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = ['name', 'created']
    readonly_fields = ['name', 'created']

admin.site.register(Order, OrderAdmin)


class ProductsAdminForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = '__all__'


class ProductsAdmin(admin.ModelAdmin):
    form = ProductsAdminForm
    list_display = ['Category', 'name', 'metal', 'stone']
    readonly_fields = ['Category', 'name', 'metal', 'stone']

admin.site.register(Products, ProductsAdmin)
