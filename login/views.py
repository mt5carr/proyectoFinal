from django.shortcuts import render, redirect
from login.forms import UserRegisterForm
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.
def register(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('inicio'))
    else:
        formulario = UserRegisterForm()
    return render(
        request= request,
        template_name= 'login/registro.html',
        context= {'formulario': formulario}
    )

