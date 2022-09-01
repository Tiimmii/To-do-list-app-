from django import forms
from . models import Task
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            )


class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'status',            

        )

class UsersignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username",)
        field_classes = {"username": UsernameField}