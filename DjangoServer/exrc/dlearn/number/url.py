from django.urls import re_path as url
from exrc.dlearn.number import views

urlpatterns = [
    url(r'number', views.number)
]
