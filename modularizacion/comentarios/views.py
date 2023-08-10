from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

# Create your views here.
def test(resquest):
    return HttpResponse("Funciona correctamente")

def create(resquest):
    #comment = Comment(name="Carlos", score=5, comment="Este es un comentario")
    #comment.save()
    comment = Comment.objects.create(name="Manuel", score=3, comment="Esta es una prueba")
    
    return HttpResponse("Eres lo máximo")

def delete(request):
    #comment = Comment.objects.get(id=1)
    #comment.delete()
    Comment.objects.filter(id=2).delete()
    return HttpResponse("Objecto 2 eliminado")