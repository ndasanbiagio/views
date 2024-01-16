from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola Mundo")

def segundaVista(request):
    return HttpResponse("<h1>Ya somos programadores de los buenos!!!</h1>")

def dia(request):
    variable = datetime.now()
    return HttpResponse(f"Hoy es un gran dia {variable}")

def apellido(request, ape):
    fecha = datetime.now()
    return HttpResponse(f"Yo soy el profe {ape}, es muy bueno <br><br> ... por lo menos hoy: {fecha}")

def cuantosAniosTengo(request, nac):
    anio_de_nacimiento = int(nac)
    anio_actual = datetime.now().year
    edad = anio_actual - anio_de_nacimiento
    return HttpResponse(f"Tu edad es: {edad}")


#Lectura de archivos
def probantoTemplate(request):
    miHTML = open("F:/Python/newproject/Proyecto1/Proyecto1/plantillas/template1.html")
    plantilla = Template(miHTML.read())
    miHTML.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)