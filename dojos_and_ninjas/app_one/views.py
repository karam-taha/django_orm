from django.shortcuts import render,redirect
from django.contrib.auth.models import *
from .models import *

def index(request):
    context={
        'dojos': Dojo.objects.all(),
        'ninjas':Ninja.objects.all()
    }
    return render (request,"index.html",context)

def new_dojo(request):
    if request.method == "POST":
        c= Dojo.objects.create(name=request.POST['name'],city=request.POST['city']
        ,state=request.POST['state'])
    return redirect('/')

def new_ninja(request):
    if request.method == "POST":
        c= Ninja.objects.create(first_name=request.POST['first-name'],last_name=request.POST['last-name'],
        dojo=Dojo.objects.get(id=request.POST['dojo']))
    return redirect('/')

