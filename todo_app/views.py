from django.shortcuts import redirect, render
from .models import Task

# Create your views here.

def home(request):
    '''Renders the home page when the user is logged in'''
    my_tasks =Task.objects.all()
    return render(request,'users.html',{'my_tasks':my_tasks})

def index(request):
    '''return the page before logging in'''
    return render(request,'index.html')

def edit(request):
    '''allows for editing the page'''
    return render(request,'edit.html')

def log(request):
    '''allows users log in'''
    return render(request,'log.html') 

def profile(request):
    '''allows to see a profile'''
    return render(request,'profile.html')

def sign(request):
    '''allows to sign in'''
    return render(request,'sign.html')

def add_task(request):
    '''Add a task to the database'''
    if request.method == 'POST':
        task_passed = request.POST.get('task')
        if task_passed:
            new_task = Task()              # instatiating a new task
            new_task.name = task_passed 
            new_task.save()
    return redirect('home')


def delete(request):
    '''delete a task from the the database'''
    deleted_item = request.GET.get('item_to_delete')
    print(deleted_item)
    del_item = Task.objects.get(id=deleted_item)
    print(del_item)
    del_item.delete()
    return redirect('home')

def edit_task(request):
    '''displaying the inner edit text'''
    if request.method == 'POST':
        text = request.POST.get('edit_text')
        id = request.POST.get('edit_id')
        if id:
            item_to_edit = Task.objects.get(id=id)
            item_to_edit.name=text
            item_to_edit.save()
    return redirect('home')
