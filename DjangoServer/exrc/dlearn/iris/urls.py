from django.urls import re_path as url
from exrc.dlearn.iris import views

urlpatterns = [
    url(r'iris', views.iris)
]

