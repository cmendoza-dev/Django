from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date
# Create your views here.
def create(request):
    rep = Reporter(first_name='Carlos', last_name='Mendoza', email='cmendoza@gmail.com')
    rep.save()

    art1 = Article(headline='Lorem ipsum dolot', pub_date=date(2022,7,5), reporter=rep)
    art1.save()
    art2 = Article(headline='Lorem set aimet', pub_date=date(2022,3,5), reporter=rep)
    art2.save()
    art3 = Article(headline='dolot aimet lorem', pub_date=date(2022,2,3), reporter=rep)
    art3.save()

    #result = art1.reporter.first_name

    result = rep.article_set.all()

    return HttpResponse(result)