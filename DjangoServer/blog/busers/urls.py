from django.urls import re_path as url
from blog.busers import views

urlpatterns = [
    url(r'busers', views.busers),
    url(r'busers_lsit', views.busers_list),
]