from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'customer', api.CustomerViewSet)
router.register(r'order', api.OrderViewSet)
router.register(r'product', api.ProductViewSet)



urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/shop', include(router.urls)),
)

urlpatterns += (
    # urls for Customer
    path('shop/customer/showAll/', views.showCustomers.as_view(), name='show_all_customers'),
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
    # urls for Product
    path('shop/product/', views.ProductListView.as_view(), name='shop_product_list'),
    path('shop/product/create/', views.ProductCreateView.as_view(), name='shop_product_create'),
    path('shop/product/detail/<slug:slug>/', views.ProductDetailView.as_view(), name='shop_product_detail'),
    path('shop/product/update/<slug:slug>/', views.ProductUpdateView.as_view(), name='shop_product_update'),
)

