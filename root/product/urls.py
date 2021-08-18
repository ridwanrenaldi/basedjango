from django.urls import path

from product import views

app_name = 'product'
urlpatterns = [
  path('', views.index, name='index'),
  path('add', views.add, name='add'),
  path('edit/<int:id>', views.edit, name='edit'),
  path('delete/<int:id>', views.delete, name='delete'),
]