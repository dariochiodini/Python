from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Comment

# Create your views here.
def test(request):
    return HttpResponse("Funciona Correctamente")

def create(request):
    #comment = Comment(name="Dario", score=5, comment="Comentario")
    #comment.save()
    comment = Comment.objects.create(name="Javier")
    return HttpResponse("probando creacion de modelos")

def delete(request):
    comment = Comment.objects.get(id=5)
    comment.delete()    
    return HttpResponse("Ruta para probar el borrado")
