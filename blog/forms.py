from django import forms
#from ckeditor.fields import RichTextField
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from blog.models import EntradaDeBlog, Post

class FormEntrada(ModelForm):
    class Meta:
        model = EntradaDeBlog
        fields = ['titulo','subtitulo', 'autor', 'cuerpo']




#borrame ------------------------------------------------------------
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','body']