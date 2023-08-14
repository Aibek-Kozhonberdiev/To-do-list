from django.urls import path
from .views import index, create_task, article_task, editing_task

urlpatterns = [
    path('', index, name='main'),
    path('task/', article_task, name='task'),
    path('task/editing/', editing_task),
    path('task/add/', create_task, name='create_task'),
]
