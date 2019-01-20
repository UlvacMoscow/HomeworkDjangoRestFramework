from django.contrib import admin
from .models import Category, Metal, Product, Stone
from customer.models import Customer
from order.models import Order


admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Metal)
admin.site.register(Stone)
