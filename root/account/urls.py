from os import name
from django.urls import path

from account import views

app_name = 'account'
urlpatterns = [
  path('', views.index, name='index'),
  path('add/', views.add, name='add'),
  path('edit/<int:id>', views.edit, name='edit'),
  path('delete/<int:id>', views.delete, name='delete'),
]