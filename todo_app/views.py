from django.shortcuts import render ,redirect
from .models import *

# Create your views here.

def home(request):
    if request.method == "POST":
        data = request.POST
        title = data.get("title")
        description = data.get("description")
        Todo.objects.create(title = title , description = description)
        
    quaryset = Todo.objects.all()
    context = {
        "todo": quaryset
    }
    return render(request , "home.html" , context)


def delete_todo(request, id):
    delete = Todo.objects.get(id = id)
    delete.delete()
    return redirect("/")

def update_todo(request ,id):
    update = Todo.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        title = data.get("title")
        description = data.get("description")
        
        update.title = title
        update.description = description
        
        update.save()
        return redirect("/")
    context = {
        "todo" : update
    }
    return render(request , "update_todo.html" , context)