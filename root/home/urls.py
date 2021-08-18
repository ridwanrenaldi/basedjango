from django.urls import path
from django.contrib.auth.views import LoginView

from home import views

app_name = 'home'
urlpatterns = [
  path('', views.index, name='index'),
  path('signin/', views.signin, name='signin'),
  path('signout/', views.signout, name='signout')
]