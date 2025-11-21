from django.http import HttpResponse
from .models import Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
def index(request):
    return HttpResponse("Привет, это мой первый Django-проект!")
# Create your views here.

def tasks_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks_list.html", {"tasks": tasks})


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')
    else:
        form = TaskForm()
    return render(request, "task_form.html", {"form": form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')
    else:
        form = TaskForm(instance=task)

    return render(request, "task_form.html", {"form": form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect('tasks_list')
    return render(request, "task_confirm_delete.html", {"task": task})