from django.shortcuts import render, redirect
from .models import Task
from .forms import UserRegisterForm, TaskForm
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, "task/register.html", {'form' : form})

@login_required
def dashboard(request):
    context = {
        'tasks' : Task.objects.all()
    }
    return render(request, "task/dashboard.html", context)

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'task/add_task.html', {'form': form})