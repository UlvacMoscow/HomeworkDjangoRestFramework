from django.urls import path, include
# from rest_framework import routers

# from . import api
from . import views

# router = routers.DefaultRouter()
# router.register(r'customer', api.CustomerViewSet)
# router.register(r'order', api.OrderViewSet)
# router.register(r'products', api.ProductsViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    # path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Customer
    path('shop/customer/', views.CustomerListView.as_view(), name='shop_customer_list'),
    path('shop/customer/create/', views.CustomerCreateView.as_view(), name='shop_customer_create'),
    path('shop/customer/detail/<int:pk>/', views.CustomerDetailView.as_view(), name='shop_customer_detail'),
    path('shop/customer/update/<int:pk>/', views.CustomerUpdateView.as_view(), name='shop_customer_update'),
)

urlpatterns += (
    # urls for Order
    path('shop/order/', views.OrderListView.as_view(), name='shop_order_list'),
    path('shop/order/create/', views.OrderCreateView.as_view(), name='shop_order_create'),
    path('shop/order/detail/<int:pk>/', views.OrderDetailView.as_view(), name='shop_order_detail'),
    path('shop/order/update/<int:pk>/', views.OrderUpdateView.as_view(), name='shop_order_update'),
)

urlpatterns += (
    # urls for Products
    path('shop/products/', views.ProductsListView.as_view(), name='shop_products_list'),
    path('shop/products/create/', views.ProductsCreateView.as_view(), name='shop_products_create'),
    path('shop/products/detail/<int:pk>/', views.ProductsDetailView.as_view(), name='shop_products_detail'),
    path('shop/products/update/<int:pk>/', views.ProductsUpdateView.as_view(), name='shop_products_update'),
)