from . import models

from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Customer
        fields = (
            'pk', 
            'name', 
            'created', 
            'phone', 
            'mail', 
        )


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = (
            'pk', 
            'name', 
            'created', 
        )


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = (
            'slug', 
            'name', 
            'created', 
        )


