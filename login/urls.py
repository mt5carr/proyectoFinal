from django.urls import path
from login.views import register, login_view, CustomLogoutView, ProfileUpdateView, agregar_avatar

urlpatterns = [

    path("signup/", register, name="registro"),
    path("login/", login_view, name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("profile/" , ProfileUpdateView.as_view(), name="editar_perfil"),
    path('agregar-avatar', agregar_avatar, name="agregar_avatar"),


]