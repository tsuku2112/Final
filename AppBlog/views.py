from django.shortcuts import render
from django.http import HttpResponse

from AppBlog.models import *

from django.core import serializers

from AppBlog.forms import *


# Create your views here.
def autor(request):
    return render(request,"AppBlog/autor.html")

def categorias(request):
    return render(request,"AppBlog/categorias.html")

def buscarBlog(request):
    titulo=request.GET["titulo"]
    total=Blog.objects.filter(titulo__contains=titulo)
    return render(request,"AppBlog/resultadoblog.html",{"resultado":total})

def buscarAutor(request):
    buscar=request.GET.get("apellido", None)
    total=Autor.objects.filter(apellido__contains=buscar)
    return render(request,"AppBlog/resultadoautor.html",{"resultado":total})

def buscarCategoria(request):
    nombre=request.GET["nombre"]
    total=Categoria.objects.filter(nombre__contains=nombre)
    return render(request,"AppBlog/resultadocategoria.html",{"resultado":total})

def inicio(request):
    return render(request,"AppBlog/inicio.html")

def blog(request):
        if request.method == "POST":
                miFormulario = BlogFormulario(request.POST) # Aqui me llega la informacion del html
                print(miFormulario)
    
                if miFormulario.is_valid:
                    informacion = miFormulario.cleaned_data
                    blog = Blog(titulo=informacion["Titulo"], publicacion=informacion["Fecha"],
                                contenido=informacion["Contenido"])
                    blog.save()
                    return render(request, "AppBlog/inicio.html")
        else:
                    miFormulario = BlogFormulario()
    
        return render(request, "AppBlog/blog.html", {"miFormulario": miFormulario})
    

def autor(request):
        if request.method == "POST":
                miFormulario = BlogFormulario(request.POST) # Aqui me llega la informacion del html
                print(miFormulario)
    
                if miFormulario.is_valid:
                    informacion = miFormulario.cleaned_data
                    blog = Blog(titulo=informacion["Titulo"], publicacion=informacion["Fecha"],
                                contenido=informacion["Contenido"])
                    blog.save()
                    return render(request, "AppBlog/inicio.html")
        else:
                    miFormulario = BlogFormulario()
    
        return render(request, "AppBlog/blog.html", {"miFormulario": miFormulario})


def blogApi(request):
    blog_todos= Blog.objects.all()
    return HttpResponse(serializers.serialize("json",blog_todos))


from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView

#Lista
class BlogList(ListView):
    model=Blog
    template="AppBlog/blog_list.html"

class AutorList(ListView):
    model=Autor
    template="AppBlog/autor_list.html"
    
class CateList(ListView):
    model=Categoria
    template="AppBlog/categoria_list.html"
    
    
#Crear    
class BlogCreate(CreateView):
    model=Blog
    fields="__all__"
    success_url="/AppBlog/blog/list"
    
class AutorCreate(CreateView):
    model=Autor
    fields="__all__"
    success_url="/AppBlog/autor/list"
    
class CateCreate(CreateView):
    model=Categoria
    fields="__all__"
    success_url="/AppBlog/cate/list"
    
#Editar
class BlogEdit(UpdateView):
    model=Blog
    fields="__all__"
    success_url="/AppBlog/blog/list"
    
class AutorEdit(UpdateView):
    model=Autor
    fields="__all__"
    success_url="/AppBlog/autor/list"
    
class CateEdit(UpdateView):
    model=Categoria
    fields="__all__"
    success_url="/AppBlog/cate/list"
    
#Detalles
class BlogDetail(DetailView):
    model=Blog
    template="AppBlog/blog_detail.html"
    
class AutorDetail(DetailView):
    model=Autor
    template="AppBlog/autor_detail.html"
    
class CateDetail(DetailView):
    model=Categoria
    template="AppBlog/categoria_detail.html"
    
#Borrar
class BlogDelete(DeleteView):
    model=Blog
    success_url="/AppBlog/blog/list"
    
class AutorDelete(DeleteView):
    model=Autor
    success_url="/AppBlog/autor/list"
    
class CateDelete(DeleteView):
    model=Categoria
    success_url="/AppBlog/cate/list"