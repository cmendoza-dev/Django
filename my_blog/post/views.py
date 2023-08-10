from django.shortcuts import render
from .models import Author, Entry
from django.http import HttpResponse

# Create your views here.

def update(resquest):
    author = Author.objects.get(id=1)
    author.name = "Carlos"
    author.email = "carlos@gmail.com"
    author.save()
    return HttpResponse("Modificado")

def queries(resquest):
    #Obtener todos los elementos
    authors = Author.objects.all()

    #Obtner datos filtrados por condición
    filtered = Author.objects.filter(email='bonnie18@example.net')

    #Obtener un único objeto (filtrado)
    author = Author.objects.get(id=1)

    # Obtener los 10 primeros elementos
    limit = Author.objects.all()[:10]

    # Obtener los 10 elementos saltando los 5 primeros
    offsets = Author.objects.all()[5:10]

    return render(resquest, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author': author, 'limit': limit, 'offsets':offsets})
