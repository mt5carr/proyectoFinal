from django.shortcuts import render, redirect
from login.forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.urls import reverse, reverse_lazy

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

def login_view(request):
    next_url = request.GET.get('next')    
    if request.method == "POST":
        formulario = AuthenticationForm(request, data = request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = data.get('username')
            psw = data.get('password')
            user = authenticate(username=usuario, password=psw) #si no autentica devuelve Null
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                return redirect(reverse('inicio'))
    else:
        formulario = AuthenticationForm()
    return render(
        request=request,
        template_name= 'login/login.html',
        context= {'formulario':formulario}
    )
        

class CustomLogoutView(LogoutView):
    template_name = 'login/logout.html'
    next_page = reverse_lazy('inicio')