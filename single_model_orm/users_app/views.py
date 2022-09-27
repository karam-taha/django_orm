from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import User

def index(request):
    context={
        'users': User.objects.all()
    }
    return render (request,"index.html",context)

def add(request):
    if request.method == "POST":
        
        c= User.objects.create(first_name=request.POST['first-name'],last_name=request.POST['last-name']
        ,email_address=request.POST['email'],age=request.POST['age'])
        c.save()
    return redirect('/')

def delete(request):
    if request.method == "POST":
        c= User.objects.get(id=request.POST['id'])
        c.delete()
    return redirect('/')

