from django.urls import re_path as url
from nlp.samsung_report import views

urlpatterns = [
    url(r'samsung', views.samsung),
]