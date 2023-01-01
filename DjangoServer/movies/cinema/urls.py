from django.urls import re_path as url
from movies.cinema import views

urlpatterns = [
    url(r'cinema', views.cinema),
    url(r'cinema_list', views.cinema_list),
]