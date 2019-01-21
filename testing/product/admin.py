from django.contrib import admin
from .models import Category, Metal, Product, Stone
from customer.models import Customer
from order.models import Order
from django import forms



# admin.site.register(Customer)
# admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Metal)
admin.site.register(Stone)

class CustomerAdminForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'


class CustomerAdmin(admin.ModelAdmin):
    form = CustomerAdminForm
    list_display = ['name', 'phone', 'email', 'has_orders', 'give_products']
    readonly_fields = ['name', 'phone', 'email']

admin.site.register(Customer, CustomerAdmin)


class OrderAdminForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'


class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = ['product', 'customer', 'creater']
    readonly_fields = ['product', 'customer', 'creater']

admin.site.register(Order, OrderAdmin)
