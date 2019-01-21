from django.urls import path
from .views import *
from . import views



urlpatterns = [
    path('order/', OrderListView.as_view() , name='app_order_list'),
    path('order/create/', views.OrderCreateView.as_view(), name='app_order_create'),
    path('order/detail/<int:pk>/', views.OrderDetailView.as_view(), name='app_order_detail'),
    path('order/update/<int:pk>/', views.OrderUpdateView.as_view(), name='app_order_update'),
    path('customer/', views.CustomerListView.as_view(), name='app_customer_list'),
]