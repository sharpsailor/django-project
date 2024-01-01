from django.http import HttpResponse
from django.shortcuts import redirect, render
from todo_app.models import TaskList
from todo_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Task Added Successfully")
            return redirect("todolist")
    else:
        all_tasks = TaskList.objects.all()
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get("page")
        all_tasks = paginator.get_page(page)
        return render(request, "todolist.html", {"all_tasks": all_tasks})


def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect("todolist")


def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task Edited Successfully")
            return redirect("todolist")
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, "edit.html", {"task_obj": task_obj})


def contact(request):
    context = {"contact_text": "Welcome to the contact page"}
    return render(request, "contact.html", context)


def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()
    return redirect("todolist")


def incomplete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect("todolist")


def about(request):
    context = {"about_text": "Welcome to the about page"}
    return render(request, "about.html", context)


def index(request):
    context = {"index_text": "Welcome to the Index page"}
    return render(request, "index.html", context)
