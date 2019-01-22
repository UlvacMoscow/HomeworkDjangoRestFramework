from django.db import models
# from order.models import order


class Customer(models.Model):
    name = models.CharField(verbose_name="Имя",max_length=50)
    phone = models.CharField(verbose_name="Телефон", max_length=25)
    email = models.EmailField(verbose_name="Почта", max_length=255)

    def __str__(self):
        return self.name

    # написать метод который определяет, были ли у человека заказы
    def has_orders(self):
        return self.customers.all().count()

    #написать метод который выводил список заказанных товаров product
    def list_orders(self):
        return self.customers.all()

        # return self.products.all()
        # return self.order.all().count()
