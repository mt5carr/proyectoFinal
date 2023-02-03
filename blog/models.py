from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

class EntradaDeBlog(models.Model):
    titulo = models.CharField(max_length=128)
    subtitulo = models.CharField(max_length=256)
    autor = models.CharField(max_length=64)    
    cuerpo = RichTextUploadingField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)
    
    def __str__(self):
        return self.titulo



