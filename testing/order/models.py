from django.db import models

from product.models import Product
from customer.models import Customer 
from django.urls import reverse



class Order(models.Model):
    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.CASCADE, related_name="products")
    customer = models.ForeignKey(Customer, verbose_name="Заказчик", on_delete=models.CASCADE, related_name="customers")
    creater = models.DateTimeField(verbose_name="Дата создание:", auto_now_add=True)

    def __str__(self):
        return self.product.title

    # def get_absolute_url(self):
    #     return reverse('app_order_detail', args=(self.pk))
