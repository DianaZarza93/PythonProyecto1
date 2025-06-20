from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil',views.perfil, name='perfil'),
    path('editar_perfil', views.editar_perfil, name='editar_perfil'),
]