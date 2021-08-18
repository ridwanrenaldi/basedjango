from django import forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class FormAccount(UserCreationForm):


  class Meta:
    model = User
    fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
    # fields = ['id','password','is_superuser','username','first_name','last_name','email','is_staff','is_active']
    widgets = {
      'username' : forms.TextInput({'class':'form-control'}),
      'email' : forms.TextInput({'class':'form-control'}),
      'first_name' : forms.TextInput({'class':'form-control'}),
      'last_name' : forms.TextInput({'class':'form-control'}),
      'password1' : forms.TextInput({'class':'form-control'}),
      'password2' : forms.TextInput({'class':'form-control'}),
    }