from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tasks
from django.forms import SelectDateWidget

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        exclude = ['status']
        fields = ['name', 'assign_to', 'priority', 'deadline', 'remarks']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'assign_to', 'status', 'priority', 'deadline', 'remarks']