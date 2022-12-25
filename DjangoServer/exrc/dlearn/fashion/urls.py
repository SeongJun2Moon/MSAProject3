from django.urls import re_path as url
from exrc.dlearn.fashion import views

urlpatterns = [
    url(r'fashion', views.fashion),
    url(r'fashion/(?P<id>)$', views.fashion),
]

