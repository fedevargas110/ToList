from django.shortcuts import render, redirect
from ToDoList.models import *
from .forms import *

def mostrar(request):
    list = Lista.objects.order_by('-fecha')
    form = ListaForm()
    ctx = {'list' : list, 'form' : form}
    return render(request, "base.html", ctx)

def archivados(request):
    list = Lista.objects.order_by('-fecha')
    ctx = {'list' : list}
    return render(request, "second.html", ctx)

def post(request):
    texto = request.POST.get("texto")
    post = Lista(texto=texto)
    post.save()
    return redirect("home")

def borrar(request, id):
    post = Lista.objects.get(pk=id)
    post.delete()
    return redirect("home")

def archivar(request, id):
    post = Lista.objects.get(pk=id)
    post.archivado=True
    post.save()
    return redirect("archivados")
# Create your views here.
