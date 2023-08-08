from django.urls import path
from .views import index, create_task, article_task

urlpatterns = [
    path('', index),
    path('article/', article_task),
    path('task/add/', create_task),
]
