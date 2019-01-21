from django.shortcuts import render
# from .models import Customer
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from order.models import Order
from .models import Customer
from order.forms import CustomerForm, OrderForm



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
