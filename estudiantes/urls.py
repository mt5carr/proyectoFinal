from django.urls import path

from estudiantes.views import saludar

urlpatterns = [
    path('saludar/', saludar)
]