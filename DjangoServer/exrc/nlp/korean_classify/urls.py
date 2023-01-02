from django.urls import re_path as url
from exrc.nlp.korean_classify import views

urlpatterns = [
    url(r'koreanClassify', views.koreanClassify),
]