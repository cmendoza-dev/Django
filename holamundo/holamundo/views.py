from django.http import HttpResponse

def saludo(resquest):
    return HttpResponse("Hola gente de sok")

def despedida(resquest):
    return HttpResponse("Cada vez que te veo solo digo adios")

def adulto(resquest, edad):
    if edad >= 18:
        return HttpResponse("Es mayor de edad")
    else:
        return HttpResponse("No eres menor de edad")