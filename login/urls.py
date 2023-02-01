from django.urls import path
from login.views import register

urlpatterns = [

    path("signup/", register, name="registro"),

]