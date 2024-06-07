from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from django.utils import timezone

class TaskForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=timezone.now().date(),
        label='Date'
    )
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        initial=timezone.now().time(),
        label='Time'
    )
    class Meta:
        model = Task
        fields = ['title', 'date', 'time', 'user']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    address = forms.CharField(max_length=100) 
    latitude = forms.FloatField()  
    longitude = forms.FloatField()  

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'address', 'latitude', 'longitude']  