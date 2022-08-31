from django import forms
from . models import Task, User
from django.contrib.auth.forms import UserCreationForm, UsernameField

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            )

class TaskViewForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'complete',
            
        )

class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',            

        )

class UsersignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}