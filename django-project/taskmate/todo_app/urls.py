from django.urls import path
from . import views

urlpatterns = [
    path("", views.todolist, name="todolist"),
    path("delete/<task_id>", views.delete_task, name="delete_task"),
    path("edit/<task_id>", views.edit_task, name="edit_task"),
    path("complete/<task_id>", views.complete_task, name="complete_task"),
    path("incomplete/<task_id>", views.incomplete_task, name="incomplete_task"),
    # path("todolist/", views.todolist, name="todolist"),
]
