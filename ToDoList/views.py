from django.shortcuts import render, redirect
from ToDoList.models import *
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def mostrar(request):
    list = Lista.objects.all()
    return render(request, "base.html", {'list': list})

# Create your views here.
