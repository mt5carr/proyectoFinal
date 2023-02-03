from django import forms
#from ckeditor.fields import RichTextField
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from blog.models import EntradaDeBlog

class FormEntrada(ModelForm):
    class Meta:
        model = EntradaDeBlog
        fields = ['titulo','subtitulo', 'autor', 'cuerpo', 'imagen']


