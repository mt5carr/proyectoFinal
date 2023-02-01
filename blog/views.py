from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from blog.models import EntradaDeBlog
from datetime import datetime
from blog.forms import FormEntrada
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect ###
from.models import Post ###
from.forms import PostForm ###
#from django.db.models import Q

def inicio(request):
    return render(
        request=request, 
        template_name='blog/inicio.html'
        )

def entradas(request):
    entradas = EntradaDeBlog.objects.all()
    contexto = {
        'entradas_ordenadas': reversed(entradas), 'entradas': entradas
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
        formulario = FormEntrada(request.POST)
        if formulario.is_valid():
            formulario.save()
        return redirect(reverse('entradas')) 
    else:
        formulario = FormEntrada()
    return render(
        request=request,
        template_name='blog/nueva_entrada.html',
        context={'formulario':formulario }
    )



def editar_entrada(request, id):    
    entrada = EntradaDeBlog.objects.get(id=id)
    if request.method == "POST":
        formulario = FormEntrada(request.POST)

        if formulario.is_valid():            
            data = formulario.cleaned_data
            entrada.titulo = data['titulo']
            entrada.subtitulo = data['subtitulo']
            entrada.autor = data['autor']
            entrada.cuerpo = data['cuerpo']        
            entrada.save()
            return redirect(reverse('entradas')) 
    else:
        inicial = {
            'titulo' : entrada.titulo, 
            'subtitulo' : entrada.subtitulo, 
            'autor' : entrada.autor, 
            'cuerpo' : entrada.cuerpo, 
        }
        formulario = FormEntrada(initial=inicial)
    return render(
        request=request,
        template_name='blog/editar_entrada.html',
        context={'formulario':formulario, 'entrada' : entrada, 'is_update' : True}
    )


def eliminar_entrada(request, id):
    entrada = EntradaDeBlog.objects.get(id=id)
    if request.method == "POST":
        entrada.delete()
        return redirect(reverse('entradas')) 
    return render(
    request=request,
    template_name='blog/confirmar_eliminar.html',
    context={'entrada' : entrada}
    )
    









#borrame ------------------------------------------------------------
def index(request):

    form = None
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:

        form = PostForm()
    return render(request, template_name='blog/index.html',context={'form':form})






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
    



