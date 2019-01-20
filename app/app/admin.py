from Order.models import Order, Item, User
from shop.models import Category, Metal, Stone, Item



admin.site.register(Order)
admin.site.register(Item, User)
admin.site.register(Category, Metal, Stone, Item)
