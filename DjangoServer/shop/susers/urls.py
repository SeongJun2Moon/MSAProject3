from django.urls import re_path as url
from shop.products import views

urlpatterns = [
    url(r'products', views.products),
    url(r'products_list', views.products_list),
]