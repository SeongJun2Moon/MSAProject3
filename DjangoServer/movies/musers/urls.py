from django.urls import re_path as url
from movies.musers import views

urlpatterns = [
    url(r'musers', views.musers),
    url(r'musers_list', views.musers_list),
]