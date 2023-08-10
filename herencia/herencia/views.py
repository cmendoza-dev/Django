from django.shortcuts import render

def herencia(request):
    return render(request, 'herencia.html', {})

def inclusion(request):
    return render(request, 'include.html', {})

def ejemplo(request):
    return render(request, 'ejemplo.html', {})

def index(request):
    return render(request, 'index.html', {})