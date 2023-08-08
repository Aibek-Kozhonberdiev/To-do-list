from django.shortcuts import render, HttpResponse
from django.core.exceptions import ValidationError
from .models import Task

def index(request):
    task = Task.objects.order_by('-date_of_completion')
    status = Task().status_choices
    context = {'task': task, 'status': status}
    return render(request, 'index.html', context)

def article_task(request):
    pk = request.GET.get('pk')
    task = Task.objects.get(pk=pk)
    status = Task.status_choices
    return render(request, 'task_view.html', {'task': task, 'status': status})

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html')

    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        status = request.POST.get('status')
        date = request.POST.get('date_of_completion')
        try:
            Task.objects.create(title=title, description=content, status=status, date_of_completion=date)
            return HttpResponse('<h1>Задача успешно записана<h1/>\n<a href="/">На главную</a>')
        except ValidationError: 
            context = {'title': title, 'content': content, 'error': True}
            return render(request, 'create_task.html', context)
