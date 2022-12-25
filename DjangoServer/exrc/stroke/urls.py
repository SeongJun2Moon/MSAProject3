from django.urls import re_path as url
from exrc.stroke import views

urlpatterns = [
    url(r'stroke', views.stroke)
]

