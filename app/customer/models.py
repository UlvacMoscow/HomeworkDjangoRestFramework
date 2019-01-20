from django.db import models



class Customer(models.Model):
    name = models.CharField(verbose_name="Имя",max_length=50)
    phone = models.CharField(verbose_name="Телефон", max_length=25)
    email = models.EmailField(verbose_name="Почта", max_length=255)

    def __str__(self):
        return self.name
