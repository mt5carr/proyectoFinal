from django.db import models

class EntradaDeBlog(models.Model):
    titulo = models.CharField(max_length=128)
    subtitulo = models.CharField(max_length=256)
    autor = models.CharField(max_length=64)
    #fecha_entrada = models.DateField(null=True)
    cuerpo = models.TextField()
    #imagen = models.TextField()

    def __str__(self):
        return f"{self.titulo} por {self.autor}"
