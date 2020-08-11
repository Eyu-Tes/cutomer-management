from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    # valid_age = forms.BooleanField(label='18+', required=False)
    # valid_age.widget.attrs.update({'class': 'form-check-input'})

    class Meta:
        model = Order

        fields = '__all__'
        # or fields = ['customer', 'product', 'date_created', 'status']

        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'product': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'status': forms.Select(attrs={'class': 'form-control form-control-sm'}),
        }
