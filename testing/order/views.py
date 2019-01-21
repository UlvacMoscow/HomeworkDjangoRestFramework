from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from order.models import Order
from .models import Customer
from order.forms import CustomerForm, OrderForm
# Create your views here.

class OrderListView(ListView):
    model = Order