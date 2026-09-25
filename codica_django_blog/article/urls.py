# codica_django_blog/article/urls.py
from django.urls import path
from codica_django_blog.article import views

urlpatterns = [
    path('', views.index),  # Cuando accedan a /articles/
]