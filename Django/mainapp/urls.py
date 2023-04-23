from django.urls import path

from .views import index, add_product, edit_product

app_name = 'mainapp'
urlpatterns = [
    path('', index, name='index'),
    path('add_product/', add_product, name='add_product'),
    path('edit_product/<int:product_pk>', edit_product, name='edit_product'),
]