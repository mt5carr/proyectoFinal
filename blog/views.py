from django.shortcuts import render, redirect
from django.urls import reverse
from blog.models import EntradaDeBlog
from blog.forms import FormEntrada
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
        entrada_buscada = EntradaDeBlog.objects.filter(titulo__contains=data['entrada'])       
        contexto = {
            'entradas_ordenadas': entrada_buscada
            }
        return render(
            request=request, 
            template_name='blog/pages.html',
            context=contexto
            )

@login_required
def nueva_entrada(request):    
    if request.method == "POST":
        formulario = FormEntrada(request.POST)
        if formulario.is_valid():
            blog = formulario.save()
            blog.user = request.user
            blog.save()
            messages.success(request, 'Entrada subido con éxito')
        return redirect(reverse('entradas')) 
    else:
        formulario = FormEntrada()
    return render(
        request=request,
        template_name='blog/nueva_entrada.html',
        context={'formulario':formulario }
    )

@login_required
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
            messages.success(request, 'Entrada editada con éxito')
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

@login_required
def eliminar_entrada(request, id):
    entrada = EntradaDeBlog.objects.get(id=id)
    if request.method == "POST":
        entrada.delete()
        messages.info(request, 'Entrada eliminada de la base de datos')
        return redirect(reverse('entradas')) 
    return render(
    request=request,
    template_name='blog/confirmar_eliminar.html',
    context={'entrada' : entrada}
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
    

