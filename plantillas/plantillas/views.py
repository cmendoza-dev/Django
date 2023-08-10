from django.shortcuts import render

def simple(resquest):
    return render(resquest, 'simple.html', {})

def dinamico(resquest, name):
    categories = ['code', 'design', 'market', 'sale', 'business']
    context = {'name': name, 'categories': categories}
    return render(resquest, 'dinamico.html', context)