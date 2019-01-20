from django.db import models
from User.models import User
from shop.models import Item



class Order(models.Model):
    decoration = models.ForeignKey(Item)
    customer = models.ForeignKey(User)
    creater = models.DataField(verbose_name="Дата создание:", auto_now_add=True)
