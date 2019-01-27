from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import EmailField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Customer(models.Model):

    # Fields
    name = models.CharField(verbose_name="имя пользователя", max_length=255)
    created = models.DateTimeField(verbose_name="создан", auto_now_add=True, editable=False)
    phone = models.CharField(verbose_name="телефон", max_length=30)
    mail = models.EmailField(verbose_name="эл.почта")


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('shop_customer_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('shop_customer_update', args=(self.pk,))


class Order(models.Model):

    # Fields
    name = models.CharField(verbose_name="имя заказа", max_length=255)
    created = models.DateTimeField(verbose_name="создан", auto_now_add=True, editable=False)

    # Relationship Fields
    customer = models.ForeignKey( 
        'Customer',
        on_delete=models.CASCADE, related_name="customers"
    )
    order = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE, related_name="products"
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('shop_order_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('shop_order_update', args=(self.pk,))


class Product(models.Model):

    # Fields
    name = models.CharField(verbose_name="название изделия", max_length=255)
    slug = extension_fields.AutoSlugField(verbose_name="slug", populate_from='name', blank=True)
    created = models.DateTimeField(verbose_name="создано", auto_now_add=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('shop_product_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('shop_product_update', args=(self.slug,))


