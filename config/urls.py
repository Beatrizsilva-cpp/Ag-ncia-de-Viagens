from django.contrib import admin
from django.urls import path
from agencia import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('clientes/', views.listar_clientes, name='clientes'),
    path('clientes/cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/<int:id>/editar/', views.editar_cliente, name='editar_cliente'),
    path('clientes/<int:id>/excluir/', views.excluir_cliente, name='excluir_cliente'),
]