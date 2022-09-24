from django.urls import path
from . import views

urlpatterns = [
    path('list', views.posts_list, name='posts_list'),

]
