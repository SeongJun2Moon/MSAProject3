from django.urls import re_path as url
from blog.tags import views

urlpatterns = [
    url(r'posts', views.tags),
    url(r'posts_list', views.tags_list),
]