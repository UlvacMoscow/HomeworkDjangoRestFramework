from django.contrib import admin
from django import forms
from .models import Customer, Order, Product

class CustomerAdminForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'


class CustomerAdmin(admin.ModelAdmin):
    form = CustomerAdminForm
    list_display = ['name', 'created', 'phone', 'mail']
    readonly_fields = ['name', 'created', 'phone', 'mail']

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


class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ['name', 'slug', 'created']
    readonly_fields = ['name', 'slug', 'created']

admin.site.register(Product, ProductAdmin)


