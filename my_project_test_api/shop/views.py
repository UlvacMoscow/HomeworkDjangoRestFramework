from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Customer, Order, Product
from .forms import CustomerForm, OrderForm, ProductForm
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from shop.serializers import *



class showCustomers(APIView):
    #show all customers

    def get(self, request):
        allCustomers = Customer.objects.all()
        serializer = CustomerSerializer(allCustomers)
        return Response(serializer.data)

class CustomerViewSet():
    queryset = Customer.objects.all().order_by('-created')
    serializer_class = CustomerSerializer


class CustomerListView(ListView):
    model = Customer


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm


class CustomerDetailView(DetailView):
    model = Customer


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm


class OrderListView(ListView):
    model = Order


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm


class OrderDetailView(DetailView):
    model = Order


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm


class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
