from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from blog.models import EntradaDeBlog
from datetime import datetime
#from django.db.models import Q

def inicio(request):
    return render(
        request=request, 
        template_name='blog/inicio.html'
        )

def entradas(request):
    entradas = EntradaDeBlog.objects.all()
    contexto = {
        'entradas': reversed(entradas)
    }
    return render(
        request=request, 
        template_name='blog/pages.html',
        context=contexto
        ) 

def buscar_entrada(request):
    if request.method == "POST":
        data = request.POST
        entrada_buscada = EntradaDeBlog.objects.filter(entrada__contains=data['entrada'])       
        contexto = {
            'entrada': entrada_buscada
            }
        return render(
            request=request, 
            template_name='blog/pages.html',
            context=contexto
            )

def nueva_entrada(request):
    if request.method == "POST":
        data = request.POST
        nueva_entrada = EntradaDeBlog(
                                    titulo=data['titulo'], 
                                    subtitulo=data['subtitulo'], 
                                    autor = 'Matias',
                                    cuerpo = data['cuerpo']                                                                     
                                    )
        nueva_entrada.save()
        return redirect(reverse('entradas')) 
    else:
        return render(
            request=request,
            template_name='blog/nueva_entrada.html'
            )

def ver_entrada(request, id):
    entrada = EntradaDeBlog.objects.get(id=id)
    contexto = {
        'entrada': entrada
        }
    return render(
        request=request,
        template_name='blog/page.html',
        context= contexto
        )






def about(request):
    return render(
        request=request, 
        template_name='blog/about.html'
        )
    
