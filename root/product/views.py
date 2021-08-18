from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from product.models import Product
from product.forms import FormProduct


@login_required(login_url=settings.LOGIN_URL)
def index(request):
  data = {
    'title' : 'product-index',
    'data' : Product.objects.all(),
  }

  return render(request, 'product/index.html', data)

@login_required(login_url=settings.LOGIN_URL)
def add(request):
  if request.POST:
    form = FormProduct(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      messages.success(request, 'Data has been saved')
      return redirect('product:add')
    else:
      messages.error(request, form.errors)
      return redirect('product:add')

  else :
    data = {
      'title' : 'product-add',
      'form' : FormProduct(),
    }
    return render(request, 'product/add.html', data)

@login_required(login_url=settings.LOGIN_URL)
def edit(request, id):
  product = Product.objects.get(product_id=id)
  if request.POST:
    form = FormProduct(request.POST, request.FILES, instance=product)
    if form.is_valid():
      form.save()
      messages.success(request, 'Data updated successfully')
      return redirect('product:edit', id=id)
    else:
      messages.error(request, form.errors)
      return redirect('product:edit', id=id)

  else:
    data = {
      'title' : 'product-edit',
      'form' : FormProduct(instance=product),
      'product' : product,
    }
    return render(request, 'product/edit.html', data)

@login_required(login_url=settings.LOGIN_URL)
def delete(request, id):
  product = Product.objects.filter(product_id=id)
  product.delete()
  messages.success(request, 'Data deleted successfully')
  return redirect('product:index')

