from django.urls import path
from AppBlog import views

urlpatterns = [
    path("",views.inicio, name="Inicio"),
    path('blog/', views.blog, name="Blogs"),
    path('blogApi/', views.blogApi),
    path('resultadoblog/', views.buscarBlog),
    path('autor/', views.autor,name="Autor"),
    path('categorias/', views.categorias, name="Categorias"),
    path('resultadoautor/', views.buscarAutor),
    path('resultadocategoria/', views.buscarCategoria),
    
    path('blog/create/', views.BlogCreate.as_view(),name="NewBlog"),
    path('blog/edit/<pk>', views.BlogEdit.as_view(), name="EditBlog"),
    path('blog/delete/<pk>', views.BlogDelete.as_view(), name="DeleteBlog"),
    path('blog/detail/<pk>', views.BlogDetail.as_view(), name="DetailBlog"),
    path('blog/list', views.BlogList.as_view(),name="ListBlog"),
    
    path('autor/create/', views.AutorCreate.as_view(),name="NewAutor"),
    path('autor/edit/<pk>', views.AutorEdit.as_view(), name="EditAutor"),
    path('autor/delete/<pk>', views.AutorDelete.as_view(), name="DeleteAutor"),
    path('autor/detail/<pk>', views.AutorDetail.as_view(), name="DetailAutor"),
    path('autor/list', views.AutorList.as_view(),name="ListAutor"),
    
    path('cate/create/', views.CateCreate.as_view(),name="NewCate"),
    path('cate/edit/<pk>', views.CateEdit.as_view(), name="EditCate"),
    path('cate/delete/<pk>', views.CateDelete.as_view(), name="DeleteCate"),
    path('cate/detail/<pk>', views.CateDetail.as_view(), name="DetailCate"),
    path('cate/list', views.CateList.as_view(),name="ListCate"),
]