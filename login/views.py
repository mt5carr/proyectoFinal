from django.shortcuts import render, redirect
from login.forms import UserRegisterForm, UserUpdateForm, AvatarFormulario
from login.models import Avatar
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.views.generic import UpdateView
from django.contrib.auth import login, authenticate
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model= User
    form_class = UserUpdateForm
    success_url= reverse_lazy('inicio')
    template_name= 'login/formulario_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user

def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            return redirect(reverse('inicio'))
    else:
        formulario = AvatarFormulario()
    return render(
        request=request,
        template_name='login/formulario_avatar.html',
        context={'formulario': formulario}
    )