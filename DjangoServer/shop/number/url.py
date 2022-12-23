from django.urls import re_path as url
from shop.number import views

urlpatterns = [
    url(r'number', views.number)
]
