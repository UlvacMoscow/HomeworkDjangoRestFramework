from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Customer, Order, Products
from .forms import CustomerForm, OrderForm, ProductsForm


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


class ProductsListView(ListView):
    model = Products


class ProductsCreateView(CreateView):
    model = Products
    form_class = ProductsForm


class ProductsDetailView(DetailView):
    model = Products


class ProductsUpdateView(UpdateView):
    model = Products
    form_class = ProductsForm

