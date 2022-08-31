from django.shortcuts import reverse
from . models import Task
from . forms import TaskCreationForm, TaskEditForm, TaskViewForm, UserCreationForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.contrib.auth import login

class Landingpage(generic.TemplateView):
    template_name = 'landingpage.html'


class Tasklist(LoginRequiredMixin, generic.ListView):
    template_name = 'index.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super(Tasklist, self).get_context_data(**kwargs)
        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['task'] = Task.objects.filter(title__startswith = search_input)
            context['search'] = search_input
        return context

    def get_queryset(self):
        queryset = Task.objects.filter(user = self.request.user)
        return queryset

#def index(request):
#    if request.user.is_authenticated:

#        task = Task.objects.filter(user=request.user)
    
#        return render(request, 'index.html', {'task':task})
#    else:
#        return redirect('task:login')

class signup(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    
    def get_success_url(self):
        return reverse('task:task-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(signup, self).form_valid(form)

#def signup(request):
#    if request.method=='POST':
#        email=request.POST['email']
#        username=request.POST['username']
#        password=request.POST['password']
#        password2=request.POST['password2']
#        firstname=request.POST['firstname']
#        lastname=request.POST['lastname']

    
#        if len(email)>0:
#            if len(username)>0:
#                if len(password)>0:
#                    if password==password2:
#                        if User.objects.filter(email=email).exists():
#                            messages.info(request, 'Email already exists')
#                            return redirect('signup')
#                        elif User.objects.filter(username=username).exists():
#                            messages.info(request, 'username already exists')
#                           return redirect('signup')
#                        else:
#                            user = User.objects.create_user(username=username, password=password, email=email)
#                            user.save()
#                           return redirect('login')
#                    else:
#                            messages.info(request, 'passwords do not match')
#                            return redirect('signup')
#                else:
#                    messages.info(request, 'password field required')
#                    return redirect('signup')
#           else:
#               messages.info(request, 'username field required')
#                return redirect('signup')
            
#        else:
#            messages.info(request, 'email field required')
#            return redirect('signup')
#    else:
#        return render(request, 'signup.html')


class TaskView(LoginRequiredMixin, generic.DetailView):
    template_name = 'view.html'
    form_class = TaskViewForm
    queryset = Task.objects.all()
    context_object_name = 'task'

class TaskEdit(LoginRequiredMixin, generic.UpdateView):
    template_name = 'edit.html'
    form_class = TaskEditForm
    queryset = Task.objects.all()
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('task:task-list')

#def edit(request, pk):
#    task = Task.objects.get(id=pk)
#    form = TaskCreationForm(instance=task)
#    if request.method =='POST':       
#        form = TaskCreationForm(request.POST, instance=task)
#        if form.is_valid():
#            form.save()
#            messages.info(request, 'task edited successfully')
#            return redirect('/')
#        else:
#            messages.info(request, 'invalid form')
#            return redirect('create')
#    else:
#        return render(request, 'edit.html', {'form':form})


class Taskdelete(LoginRequiredMixin, generic.DeleteView):
    template_name = 'delete.html'
    queryset = Task.objects.all()
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('task:task-list')

#def delete(request, pk):
#    task=Task.objects.get(id=pk)
#    task.delete()
#    messages.info(request, 'deleted successfully')
#    return redirect('/')
    

class Taskcreate(LoginRequiredMixin, generic.CreateView):
    template_name = 'create.html'
    queryset = Task.objects.all()
    form_class = TaskCreationForm

    def get_success_url(self):
        return reverse('task:task-list')

#def create(request):
#    form = TaskCreationForm()
#    if request.method =='POST':
#        form=TaskCreationForm(request.POST)
#        if form.is_valid():
#            title=form.cleaned_data['title']
#            description=form.cleaned_data['description']
#
#            if len(title)>0:
#                current_user = request.user
#                new_task=Task.objects.create(title=title, description=description, user=current_user)
#               new_task.save()
#                messages.info(request, 'new task added successfully')
#                return redirect('/')
#            else:
#                messages.info(request, 'title field required')
#                return redirect('create')
#        else:
#            messages.info(request, 'invalid form')
#            return redirect('create')
#   else:
#       return render(request, 'create.html', {'form':form})