from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ProductForm
from .models import Product


def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'mainapp/goods_list.html', context)


def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(data=request.POST)
        if product_form.is_valid():
            product_form.save()
        return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        context = {
            'product_form': ProductForm()
        }
        return render(request, 'mainapp/good_create.html', context)


def edit_product(request, product_pk: int):
    product = Product.objects.get(pk=product_pk)
    if request.method == 'POST':
        product_form = ProductForm(instance=product, data=request.POST)
        if product_form.is_valid():
            product_form.save()
        return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        context = {
            'product_form': ProductForm(instance=product)
        }
        return render(request, 'mainapp/good_edit.html', context)
