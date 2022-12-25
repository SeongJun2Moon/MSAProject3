from django.urls import re_path as url
from exrc.dlearn.fruits import views

urlpatterns = [
    url(r'fruit', views.fruits),
]

