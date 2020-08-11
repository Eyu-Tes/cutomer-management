import django_filters
from django_filters import DateFilter
from django import forms
from .models import *


class OrderFliter(django_filters.FilterSet):

    start_date = DateFilter(field_name="date_created", lookup_expr='gte', label='furthest date')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte', label='latest date')

    class Meta:
        model = Order
        exclude = ['customer', 'date_created']
        # or fields = ['product', 'status']
