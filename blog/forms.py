from django import forms
from ckeditor.fields import RichTextField

class FormEntrada(forms.Form):
    titulo = forms.CharField(max_length=128)
    subtitulo = forms.CharField(max_length=256)
    autor = forms.CharField(max_length=64)
    #fecha_entrada = forms.DateField(null=True)
    cuerpo = forms.CharField()
    #imagen = forms.TextField() 