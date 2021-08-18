from django import forms
from django.forms import ModelForm
from category.models import Category
from django.utils.translation import gettext_lazy as _

class FormCategory(ModelForm):
  class Meta:
    model = Category
    fields = '__all__'
    labels = {
      'category_name': _('Name'),
      'category_description': _('Description'),
    }
    widgets = {
      'category_name' : forms.TextInput({'class':'form-control'}),
      'category_description' : forms.TextInput({'class':'form-control'})
    }