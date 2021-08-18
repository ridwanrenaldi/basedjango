from category.models import Category
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from account.forms import FormAccount

@login_required(login_url=settings.LOGIN_URL)
def index(request):
  data = {
    'title' : 'account-index',
    'data' : User.objects.values(),
  }
  return render(request, 'account/index.html', data)

@login_required(login_url=settings.LOGIN_URL)
def add(request):
  if request.POST:
    form = FormAccount(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Data has been saved')
      return redirect('account:add')
    else:
      messages.error(request, form.errors)
      return redirect('account:add')
  else:
    data = {
      'title' : 'account-add',
      'form' : FormAccount(),
    }
    return render(request, 'account/add.html', data)

@login_required(login_url=settings.LOGIN_URL)
def edit(request, id):
  user = User.objects.get(id=id)
  if request.POST:
    form = FormAccount(request.POST, instance=user)
    if form.is_valid():
      form.save()
      messages.success(request, 'Data updated successfully')
      return redirect('account:edit', id=id)
    else:
      messages.error(request, form.errors)
      return redirect('account:edit', id=id)
  else:
    data = {
      'title' : 'account-add',
      'form' : FormAccount(instance=user),
      'user' : user,
    }
    return render(request, 'account/edit.html', data)

@login_required(login_url=settings.LOGIN_URL)
def delete(request, id):
  user = User.objects.filter(id=id)
  user.delete()
  messages.success(request, 'Data deleted successfully')
  return redirect('account:index')