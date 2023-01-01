from django.urls import re_path as url
from movies.showtimes import views

urlpatterns = [
    url(r'showtimes', views.showtimes),
    url(r'showtimes_list', views.showtimes_list),
]