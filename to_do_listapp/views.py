from tkinter import NO
from django.shortcuts import render, redirect
from . models import Task
from django.contrib.auth.models import User, auth
from . models import User
from django.contrib import messages
from . forms import TaskCreationForm, TaskEditForm, TaskViewForm


def index(request):
    if request.user.is_authenticated:

        task = Task.objects.filter(user=request.user)
    
        return render(request, 'index.html', {'task':task})
    else:
        return redirect('login')


def signup(request):
    if request.method=='POST':
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']

    
        if len(email)>0:
            if len(username)>0:
                if len(password)>0:
                    if password==password2:
                        if User.objects.filter(email=email).exists():
                            messages.info(request, 'Email already exists')
                            return redirect('signup')
                        elif User.objects.filter(username=username).exists():
                            messages.info(request, 'username already exists')
                            return redirect('signup')
                        else:
                            user = User.objects.create_user(username=username, password=password, email=email)
                            user.save()
                            return redirect('login')
                    else:
                            messages.info(request, 'passwords do not match')
                            return redirect('signup')
                else:
                    messages.info(request, 'password field required')
                    return redirect('signup')
            else:
                messages.info(request, 'username field required')
                return redirect('signup')
            
        else:
            messages.info(request, 'email field required')
            return redirect('signup')
    else:
        return render(request, 'signup.html')



def login(request):
    if request.method=='POST':
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']

        if len(email)>0:
            if len(username)>0:
                if len(password)>0:
                    user = auth.authenticate(username=username, password=password)

                    if user is None:
                        messages.info(request,'User not found')
                        return redirect('login')
                    else:
                        auth.login(request, user)
                        return redirect('/')
                else:
                    messages.info(request, 'password field required')
                    return redirect('login')
            else:
                messages.info(request, 'username field required')
                return redirect('login')
        else:
            messages.info(request, 'email field required')
            return redirect('login')
    else:
        return render(request, 'login.html')

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        searched = Task.objects.filter(title__icontains=search)
        return render(request, 'search.html', {'search':search, 'searched':searched})
    else:
        return render(request, 'search.html',{})

def view(request, pk):
    
    view = Task.objects.get(id=pk)
    form = TaskViewForm(instance=view)
    if request.method=='POST':
        form = TaskCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'successful')
            return redirect('/')
        else:
            messages.info(request, 'unsuccessful :(')
            return redirect('/')
    else:    
        return render(request, 'view.html',{'view':view, 'form':form})

   

def edit(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskCreationForm(instance=task)
    if request.method =='POST':       
        form = TaskCreationForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.info(request, 'task edited successfully')
            return redirect('/')
        else:
            messages.info(request, 'invalid form')
            return redirect('create')
    else:
        return render(request, 'edit.html', {'form':form})



def delete(request, pk):
    query=Task.objects.get(id=pk)
    query.delete()
    messages.info(request, 'deleted successfully')
    return redirect('/')
    

def create(request):
    form = TaskCreationForm()
    if request.method =='POST':
        form=TaskCreationForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            description=form.cleaned_data['description']

            if len(title)>0:
                current_user = request.user
                new_task=Task.objects.create(title=title, description=description, user=current_user)
                new_task.save()
                messages.info(request, 'new task added successfully')
                return redirect('/')
            else:
                messages.info(request, 'title field required')
                return redirect('create')
        else:
            messages.info(request, 'invalid form')
            return redirect('create')
    else:
        return render(request, 'create.html', {'form':form})