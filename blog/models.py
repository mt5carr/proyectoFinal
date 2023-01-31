from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class EntradaDeBlog(models.Model):
    titulo = models.CharField(max_length=128)
    subtitulo = models.CharField(max_length=256)
    autor = models.CharField(max_length=64)
    #fecha_entrada = models.DateField(null=True)
    cuerpo = RichTextUploadingField()
    #imagen = models.TextField()

    def __str__(self):
        return self.titulo







#borrame ------------------------------------------------------------
class Post(models.Model):

    title = models.CharField(max_length=255)
    #body = models.TextField() 
    body = RichTextUploadingField() # CKEditor Rich Text Field

    def __str__(self):
        return self.title