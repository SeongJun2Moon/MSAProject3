from django.urls import re_path as url
from exrc.dlearn.aitrader import views

urlpatterns = [
    url(r'aitrader_samsung', views.aitrader),
]

