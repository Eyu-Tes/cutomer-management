# from django.http import HttpResponse
# from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from .models import *
from .forms import OrderForm


# Create your views here.
class HomePageView(ListView):
    model = Order
    queryset = Order.objects.order_by('-date_created')[:5]
    context_object_name = 'last5orders'
    template_name = 'accounts/dashboard.html'

    # Adding extra context
    def get_context_data(self, *, object_list=None, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['customers'] = Customer.objects.all()
        order_objects = Order.objects.all()
        context['total_orders'] = order_objects.count()
        context['delivered_orders'] = order_objects.filter(status='Delivered').count()
        context['pending_orders'] = order_objects.filter(status='Pending').count()

        return context


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 5
    template_name = 'accounts/products.html'


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'accounts/customer.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # In a class-based view, all of the elements from the URL are placed into:
        # self.args ( if they're non-named groups) or self.kwargs (for named groups).
        # this is the primary key from your URL
        pk = self.kwargs['pk']
        customer_obj = Customer.objects.get(id=pk)
        customer_orders = customer_obj.order_set.all()
        context['customer_orders'] = customer_orders
        context['order_count'] = customer_orders.count()

        return context


class OrderCreateView(SuccessMessageMixin, CreateView):
    model = Customer
    form_class = OrderForm
    extra_context = {'legend': 'Create Order'}
    success_message = "Order created successfully!"
    template_name = 'accounts/order_form.html'

    def get_initial(self):
        # Get the initial dictionary from the superclass method
        initial = super().get_initial()
        initial['customer'] = Customer.objects.get(id=self.kwargs['fk'])

        return initial

    def get_success_url(self):
        return reverse_lazy('accounts-customer', kwargs={'pk': self.kwargs['fk']})


class OrderUpdateView(SuccessMessageMixin, UpdateView):
    model = Order
    form_class = OrderForm
    extra_context = {'legend': 'Update Order'}
    success_message = "Order updated successfully!"
    template_name = 'accounts/order_form.html'

    def get_success_url(self):
        # self.object is the specific object of interest
        return reverse_lazy('accounts-customer', kwargs={'pk': self.object.customer.pk})


class OrderDeleteView(DeleteView):
    model = Order
    extra_context = {'legend': 'Delete Order'}
    success_message = "Order deleted successfully!"
    template_name = 'accounts/remove_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_fields'] = [self.object.product, self.object.customer, self.object.status]

        return context

    def get_success_url(self):
        return reverse_lazy('accounts-home')

    # success message for delete
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
