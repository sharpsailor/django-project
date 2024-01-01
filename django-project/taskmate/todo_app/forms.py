from django import forms
from todo_app.models import TaskList


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ["task", "done"]
