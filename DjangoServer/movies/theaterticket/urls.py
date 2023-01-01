from django.urls import re_path as url
from movies.theaterticket import views

urlpatterns = [
    url(r'theaterticket', views.theaterticket),
    url(r'theaterticket_list', views.theaterticket_list),
]