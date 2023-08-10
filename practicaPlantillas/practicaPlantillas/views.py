from django.shortcuts import render

def inicio(resquest):
    return render(resquest, 'index.html', {})

def portafolio(resquest):
    return render(resquest, 'portfolio.html', {})

