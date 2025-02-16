from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login, authenticate,logout
from .forms import SignUpForm, LoginForm, TaskForm
from to_do_app.models import Task


# Create your views here.



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
        
    return render(request,'todoapp/register.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            print(f'User: {user}')
            if user is not None:
                auth_login(request,user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request,'todoapp/login.html',{'form':form})

def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    else:
        form = TaskForm()
    
    all_tasks = Task.objects.filter(user = request.user)

    return render(request,'todoapp/home.html',{'form':form,'all_tasks':all_tasks})


def delete(request, name):
    get_task = Task.objects.get(user = request.user , name = name)
    get_task.delete()
    return redirect('home')

def update(request, name):
    get_task = Task.objects.get(user = request.user , name=name)
    get_task.status = True
    get_task.save()
    return redirect('home')


def user_logout(request):
    logout(request)
    return redirect('login')