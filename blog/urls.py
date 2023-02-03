from django.urls import path
from blog.views import  (
    inicio, 
    entradas, 
    buscar_entrada, 
    nueva_entrada, 
    editar_entrada, 
    eliminar_entrada, 
    ver_entrada, 
    about    
    )

urlpatterns = [

    path("", inicio, name="inicio"),
    path("pages/", entradas, name="entradas"),
    path("buscar-entrada", buscar_entrada, name="buscar_entrada"),
    path("nueva-entrada", nueva_entrada, name="crear_entrada"),    
    path("editar-entrada/<int:id>/", editar_entrada, name="editar_entrada"),   
    path("pages/<int:id>/", ver_entrada, name="ver_entrada"),
    path("eliminar-entrada/<int:id>/", eliminar_entrada, name="eliminar_entrada"),
    path("about/", about, name="sobre_mi"),
    
]
