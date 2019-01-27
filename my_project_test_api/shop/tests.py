import unittest
from django.urls import reverse
from django.test import Client
from .models import Customer, Order, Product
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_customer(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["phone"] = "phone"
    defaults["mail"] = "mail"
    defaults.update(**kwargs)
    return Customer.objects.create(**defaults)


def create_order(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "customer" not in defaults:
        defaults["customer"] = create_customer()
    if "order" not in defaults:
        defaults["order"] = create_product()
    return Order.objects.create(**defaults)


def create_product(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Product.objects.create(**defaults)


class CustomerViewTest(unittest.TestCase):
    '''
    Tests for Customer
    '''
    def setUp(self):
        self.client = Client()

    def test_list_customer(self):
        url = reverse('shop_customer_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_customer(self):
        url = reverse('shop_customer_create')
        data = {
            "name": "name",
            "phone": "phone",
            "mail": "mail",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_customer(self):
        customer = create_customer()
        url = reverse('shop_customer_detail', args=[customer.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_customer(self):
        customer = create_customer()
        data = {
            "name": "name",
            "phone": "phone",
            "mail": "mail",
        }
        url = reverse('shop_customer_update', args=[customer.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class OrderViewTest(unittest.TestCase):
    '''
    Tests for Order
    '''
    def setUp(self):
        self.client = Client()

    def test_list_order(self):
        url = reverse('shop_order_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_order(self):
        url = reverse('shop_order_create')
        data = {
            "name": "name",
            "customer": create_customer().pk,
            "order": create_product().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_order(self):
        order = create_order()
        url = reverse('shop_order_detail', args=[order.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_order(self):
        order = create_order()
        data = {
            "name": "name",
            "customer": create_customer().pk,
            "order": create_product().pk,
        }
        url = reverse('shop_order_update', args=[order.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProductViewTest(unittest.TestCase):
    '''
    Tests for Product
    '''
    def setUp(self):
        self.client = Client()

    def test_list_product(self):
        url = reverse('shop_product_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_product(self):
        url = reverse('shop_product_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_product(self):
        product = create_product()
        url = reverse('shop_product_detail', args=[product.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_product(self):
        product = create_product()
        data = {
            "name": "name",
        }
        url = reverse('shop_product_update', args=[product.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


