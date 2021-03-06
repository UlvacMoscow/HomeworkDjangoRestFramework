from django.db import models
from customer.models import Customer
from shop.models import Item



class Order(models.Model):
    item = models.ForeignKey(Item, verbose_name="Товар", on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, verbose_name="Заказчик", on_delete=models.CASCADE)
    creater = models.DateTimeField(verbose_name="Дата создание:", auto_now_add=True)
