from django.db import models
from ckeditor.fields import RichTextField

class EntradaDeBlog(models.Model):
    titulo = models.CharField(max_length=128)
    subtitulo = models.CharField(max_length=256)
    autor = models.CharField(max_length=64)
    #fecha_entrada = models.DateField(null=True)
    cuerpo = RichTextField()
    #imagen = models.TextField()

    def __str__(self):
        return f"{self.titulo} por {self.autor}"
