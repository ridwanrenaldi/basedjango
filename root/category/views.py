from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from category.models import Category
from category.forms import FormCategory
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def index(request):
  data = {
    'title' : 'category-index',
    'data' : Category.objects.all(),
  }
  return render(request, 'category/index.html', data)

@login_required(login_url=settings.LOGIN_URL)
def add(request):
  if request.POST:
    form = FormCategory(request.POST)
    if form.is_valid:
      form.save()
      messages.success(request, 'Data has been saved')
      return redirect('category:add')
    else:
      messages.error(request, 'There is an error')
      return redirect('category:add')

  else :
    data = {
      'title' : 'category-add',
      'form' : FormCategory(),
    }
    return render(request, 'category/add.html', data)

@login_required(login_url=settings.LOGIN_URL)
def edit(request, id):
  category = Category.objects.get(category_id=id)
  if request.POST:
    form = FormCategory(request.POST, instance=category)
    if form.is_valid():
      form.save()
      messages.success(request, 'Data updated successfully')
      return redirect('category:edit', id=id)
    else:
      messages.error(request, 'There is an error')
      return redirect('category:edit', id=id)

  else:
    data = {
      'title' : 'category-edit',
      'form' : FormCategory(instance=category),
      'category' : category,
    }
    return render(request, 'category/edit.html', data)

@login_required(login_url=settings.LOGIN_URL)
def delete(request, id):
  category = Category.objects.filter(category_id=id)
  category.delete()
  messages.success(request, 'Data deleted successfully')
  return redirect('category:index')