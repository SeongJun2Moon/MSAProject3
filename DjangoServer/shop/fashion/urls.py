from django.urls import re_path as url
from shop.fashion import views

urlpatterns = [
    url(r'fashion', views.fashion),
    url(r'fashion/(?P<id>)$', views.fashion),
]

