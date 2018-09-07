from django.shortcuts import render, redirect
from ToDoList.models import *

def mostrar(request):
    list = Lista.objects.all()
    ctx = {'list' : list}
    return render(request, "base.html", ctx)

# Create your views here.
