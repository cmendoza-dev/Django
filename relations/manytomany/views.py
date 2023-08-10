from django.shortcuts import render
from django.http import HttpResponse
from .models import Publication, Article

# Create your views here.
def create(request):
    art1 = Article(headline='Article 1')
    art1.save()

    art2 = Article(headline='Article 2')
    art2.save()

    art3 = Article(headline='Article 3')
    art3.save()

    pub1 = Publication(title='Publicación 1')
    pub1.save()
    pub2 = Publication(title='Publicación 2')
    pub2.save()
    pub3 = Publication(title='Publicación 3')
    pub3.save()
    pub4 = Publication(title='Publicación 4')
    pub4.save()
    pub5 = Publication(title='Publicación 5')
    pub5.save()
    pub6 = Publication(title='Publicación 6')
    pub6.save()
    pub7 = Publication(title='Publicacion 7')
    pub7.save()

    art1.publications.add(pub1)
    art1.publications.add(pub2)
    art1.publications.add(pub3)
    art2.publications.add(pub4)
    art2.publications.add(pub5)
    art3.publications.add(pub6)
    art3.publications.add(pub7)

    result = art1.publications.all()
    return HttpResponse(result)

