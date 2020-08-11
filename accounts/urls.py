from django.urls import path
from . import views
from .views import (
    HomePageView, ProductListView, CustomerDetailView,
    OrderCreateView, OrderUpdateView, OrderDeleteView)

# path(route, view, name)
urlpatterns = [
    path('', HomePageView.as_view(), name='accounts-home'),
    path('products/', ProductListView.as_view(), name='accounts-products'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='accounts-customer'),
    path('order/<int:fk>/create/', OrderCreateView.as_view(), name='accounts-create_order'),
    path('order/<int:pk>/update/', OrderUpdateView.as_view(), name="accounts-update_order"),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name="accounts-delete_order"),
]
