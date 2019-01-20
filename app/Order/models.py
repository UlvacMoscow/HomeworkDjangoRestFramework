from django.db import models

class Order(models.Model):
    decoration = models.ForeignKey(Item)
    customer = models.ForeignKey(User)
    creater = models.DataField(verbose_name="Дата создание:", auto_now_add=True)
