from django.shortcuts import render, redirect
from .models import Task

STATUS = Task().status_choices

def index(request):
    task = Task.objects.all().order_by('-date_of_completion')
    context = {'task': task, 'status': STATUS}
    return render(request, 'index.html', context)

def article_task(request):
    pk = request.GET.get('pk')
    task = Task.objects.get(pk=pk)

    if request.POST.get('delete'):
        Task.objects.filter(id=task.id).delete()
        return render(request, 'massage.html', {'title': 'Удаление', 'message': 'Задача успешно удалена'})

    return render(request, 'task_view.html', {'task': task, 'status': STATUS})

def editing_task(request):
    pk = request.GET.get('pk')
    task = Task.objects.get(pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        status = request.POST.get('status', 'new')
        date_of_completion = request.POST.get('date_of_completion')

        if title.strip() and content.strip():
            if date_of_completion:
                new_task = Task.objects.filter(id=task.id).update(title=title, description=content, status=status, date_of_completion=date_of_completion)
            else:
                new_task = Task.objects.filter(id=task.id).update(title=title, description=content, status=status)

            return render(request, 'massage.html', {'pk': task.pk, 'title': 'Обновление задачи', 'message': 'Задача успешно обновлена'})

        return render(request, 'editing.html', {'pk': task.pk, 'error': True, 'title': title, 'content': content, 'status': status, 'date_of_completion': date_of_completion, 'statuses': STATUS})

    return render(request, 'editing.html', {'task': task, 'pk': task.pk, 'statuses': STATUS})

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        status = request.POST.get('status', 'new')
        date_of_completion = request.POST.get('date_of_completion')

        if title.strip() and content.strip():
            if date_of_completion:
                new_task = Task.objects.create(title=title, description=content, status=status, date_of_completion=date_of_completion)
            else:
                new_task = Task.objects.create(title=title, description=content, status=status)

            return render(request, 'massage.html', {'title': 'Добавить задачу', 'message': 'Задача успешно добавлена'})

        return render(request, 'create_task.html', {'error': True, 'title': title, 'content': content, 'statuses': STATUS})

    return render(request, 'create_task.html', {'statuses': STATUS})
