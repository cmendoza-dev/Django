from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

def form(request):
    commentform =  CommentForm()
    return render(request, 'form.html', {'commentform': commentform})

def goal(request):
    name = request.POST['name']
    # Hacer una guarda
    if request.method != 'POST':
        return HttpResponse('Método no permitido')

    return render(request, 'success.html', {'name':name})


def widget(request):
    if request.method == 'GET':
        contact = ContactForm()
        return render(request, 'widget.html', {'contact':contact})

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #Aqui iran todos los acciones a realizar
            return HttpResponse('válido')
        else:
            
            return render(request, 'widget.html', {'form':form})

