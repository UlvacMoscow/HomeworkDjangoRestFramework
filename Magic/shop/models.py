from django.db import models
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import EmailField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Customer(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=25)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('shop_customer_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('shop_customer_update', args=(self.pk,))


class Order(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    # Relationship Fields
    customer = models.ForeignKey(
        'shop.Customer',
        on_delete=models.CASCADE, related_name="customers"
    )
    product = models.ForeignKey(
        'shop.Products',
        on_delete=models.CASCADE, related_name="productss"
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('shop_order_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('shop_order_update', args=(self.pk,))


class Products(models.Model):

    # Fields
    Category = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    stone = models.CharField(max_length=30)
    metal = models.CharField(max_length=50)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('shop_products_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('shop_products_update', args=(self.pk,))