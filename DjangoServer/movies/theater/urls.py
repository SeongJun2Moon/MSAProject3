from django.urls import re_path as url
from movies.theater import views

urlpatterns = [
    url(r'theater', views.theater),
    url(r'theater_list', views.theater_list),
]