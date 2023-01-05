from django import forms
 
class BlogFormulario(forms.Form):
    titulo=forms.CharField(max_length=40)
    subtitulo=forms.CharField(max_length=40)
    publicacion=forms.DateField()
    contenido=forms.CharField()

class AutorFormulario(forms.Form):
    apellido=forms.CharField(max_length=40)
    nombre=forms.CharField(max_length=40)
    mail=forms.EmailField()
    
class CategoriaFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    descripcion=forms.CharField(max_length=140)