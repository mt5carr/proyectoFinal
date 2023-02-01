from django.urls import path
from login.views import register, login_view, CustomLogoutView

urlpatterns = [

    path("signup/", register, name="registro"),
    path("login/", login_view, name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),

]