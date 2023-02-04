from django.forms import ModelForm
from blog.models import EntradaDeBlog

class FormEntrada(ModelForm):
    class Meta:
        model = EntradaDeBlog
        fields = ['titulo','subtitulo', 'autor', 'cuerpo']


