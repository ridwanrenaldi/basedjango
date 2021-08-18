from django import forms
from django.forms import ModelForm, fields, widgets
from product.models import Product
from django.utils.translation import gettext_lazy as _

class FormProduct(ModelForm):
  class Meta:
    model = Product
    fields = ['category', 'product_name', 'product_description', 'product_stock', 'product_image']
    label = {
      'category' : _('Category'), 
      'product_name' : _('Name'),
      'product_description' : _('Description'),
      'product_stock' : _('Stock'),
      'product_image' : _('Image'),
    }
    widgets = {
      'category' : forms.Select({'class':'form-control'}),
      'product_name' : forms.TextInput({'class':'form-control'}),
      'product_description' : forms.Textarea({'class':'form-control'}),
      'product_stock' : forms.NumberInput({'class':'form-control'}),
      'product_image' : forms.FileInput({'class':'form-control'}),
    }