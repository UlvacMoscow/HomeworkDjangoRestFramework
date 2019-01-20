from django.db import models


from customer.models import Customer
from product.models import Product



class Order(models.Model):
    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, verbose_name="Заказчик", on_delete=models.CASCADE)
    creater = models.DateTimeField(verbose_name="Дата создание:", auto_now_add=True)

    def __str__(self):
        return self.product.title
