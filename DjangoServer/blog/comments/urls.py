from django.urls import re_path as url
from blog.comments import views

urlpatterns = [
    url(r'comments', views.comments),
    url(r'comments_list', views.comments_list),
]