from django import forms

class FormLogin(forms.Form):
  # username = forms.CharField(max_length=20)
  # password = forms.CharField(widget = forms.PasswordInput())

  username = forms.CharField(
      max_length=20,
      widget=forms.TextInput(
          attrs={
              'class': 'form-control',
              'placeholder': 'Username'
          }
      )
  )

  password = forms.CharField(
      max_length=20,
      widget=forms.PasswordInput(
          attrs={
              'class': 'form-control',
              'placeholder': 'Password'
          }
      )
  )