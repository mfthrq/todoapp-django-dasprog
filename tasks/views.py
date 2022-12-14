from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

def index(request):
    tasks = Task.objects.all()
    
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html', context)

def update(request, primary_key):
    task = Task.objects.get(id=primary_key)
    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'item':task,'form':form}
    return render(request, 'tasks/update.html', context)

def deleteTask(request, primary_key):
	item = Task.objects.get(id=primary_key)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'tasks/delete.html', context)