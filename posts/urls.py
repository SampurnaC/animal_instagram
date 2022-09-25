from django.urls import path
from . import views

urlpatterns = [
    path('list', views.posts_list, name='posts_list'),
    path('create', views.create, name='post_create')
]
