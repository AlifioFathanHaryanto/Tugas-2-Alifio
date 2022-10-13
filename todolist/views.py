from django.shortcuts import render
from todolist.models import ToDoList
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from todolist.models import ToDoList
from django.http import HttpResponseBadRequest

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    task_list = []
    data_todolist = ToDoList.objects.filter(user=request.user),
    context = {
        'list_todo': data_todolist,
        'user': request.user,
        'nama': 'Alifio Fathan Haryanto',
        'npm': 2106653483,
        'last_login': request.COOKIES['last_login'],
    }
    print (request.user)
    print (data_todolist)
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.now()
        user = request.user
        todolist_object = ToDoList.objects.create(title=title, description=description, date=date, user=user)
        todolist_object.save()
        return redirect('todolist:show_todolist')
    context = {}
    return render(request, 'create_task.html', context)

@login_required(login_url='/todolist/login/')
def show_json(req):
    task_list = ToDoList.objects.filter(user=req.user)
    return HttpResponse(serializers.serialize("json", task_list), content_type="application/json")

@login_required(login_url='/todolist/login/')
def input_task(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        date = datetime.date.today()
        description = request.POST.get('description')
        todo = ToDoList.objects.create(title=title, description=description, date=date, user=user)

        result = {
            'fields':{
                'title':todo.title,
                'date':todo.date,
                'description':todo.description,
            },
            'pk':todo.pk
        }
        return JsonResponse(result)
