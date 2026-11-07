
from django.contrib import admin
from django.urls import path
from agencia import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.inicio, name='inicio'),

    # CLIENTES
    path('clientes/', views.listar_clientes, name='clientes'),
    path('clientes/cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/<int:id>/editar/', views.editar_cliente, name='editar_cliente'),
    path('clientes/<int:id>/excluir/', views.excluir_cliente, name='excluir_cliente'),

    # DESTINOS
    path('destinos/', views.listar_destinos, name='destinos'),
    path('destinos/cadastrar/', views.cadastrar_destino, name='cadastrar_destino'),
    path('destinos/<int:id>/editar/', views.editar_destino, name='editar_destino'),
    path('destinos/<int:id>/excluir/', views.excluir_destino, name='excluir_destino'),
]
