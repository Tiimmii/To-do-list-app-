from pyexpat import model
from django import forms
from . models import Task

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