from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
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
        form = ProductForm(data=request.POST)
        template_name = 'mainapp/goods_list.html'
    else:
        form = ProductForm()
        template_name = 'mainapp/good_create.html'
    return save_good_form(request, form, template_name)


def save_good_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data['html_good_list'] = render_to_string('mainapp/goods_list.html', {'products': Product.objects.all()})
        else:
            data['form_is_valid'] = False
            print(f'Ошибка валидации формы: {form.errors}')
    else:
        context = {'form': form}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


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
