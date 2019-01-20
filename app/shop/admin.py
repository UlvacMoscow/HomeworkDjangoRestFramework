from django.contrib import admin
from Order.models import Order, Customer
from .models import Category, Metal, Stone, Item



admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Metal)
admin.site.register(Stone)
