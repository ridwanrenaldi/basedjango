from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import authenticate, logout, login
from home.forms import FormLogin

@login_required(login_url=settings.LOGIN_URL)
def index(request):
  data = {
    'title' : 'home-index',
  }
  return render(request, 'home/index.html', data)

def signin(request):
  if request.user.is_authenticated:
    return redirect('home:index')
  else:
    if request.POST:
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
        if user.is_active:
          request.session.set_expiry(86400)
          login(request, user)
          return redirect('home:index')
        else:
          messages.error(request, 'Account inactive')
      else:
        messages.error(request, 'Account not found')
        return redirect('home:signin')
    else:
      data = {
        'title' : 'home-signin',
        'form' : FormLogin(),
      }
      return render(request, 'home/signin.html', data)

def signout(request):
  logout(request)
  return redirect('home:signin')
