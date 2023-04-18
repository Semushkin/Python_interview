from django import forms
from django.forms import NumberInput
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name',
                  'data_received',
                  'price',
                  'quantity',
                  'supplier')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['data_received'] = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control form-control-sm'
