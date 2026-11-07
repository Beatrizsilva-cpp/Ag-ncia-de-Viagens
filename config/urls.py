
from django.contrib import admin
from django.urls import path
from agencia import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.inicio, name='inicio'),
        # PACOTES DE VIAGEM
    path('pacotes/', views.listar_pacotes, name='pacotes'),
    path('pacotes/cadastrar/', views.cadastrar_pacote, name='cadastrar_pacote'),
    path('pacotes/<int:id>/editar/', views.editar_pacote, name='editar_pacote'),
    path('pacotes/<int:id>/excluir/', views.excluir_pacote, name='excluir_pacote'),
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

    # PACOTES DE VIAGEM
    path('pacotes/', views.listar_pacotes, name='pacotes'),
    path('pacotes/cadastrar/', views.cadastrar_pacote, name='cadastrar_pacote'),
    path('pacotes/<int:id>/editar/', views.editar_pacote, name='editar_pacote'),
    path('pacotes/<int:id>/excluir/', views.excluir_pacote, name='excluir_pacote'),

        # RESERVAS
    path('reservas/', views.listar_reservas, name='reservas'),
    path('reservas/cadastrar/', views.cadastrar_reserva, name='cadastrar_reserva'),
    path('reservas/<int:id>/editar/', views.editar_reserva, name='editar_reserva'),
    path('reservas/<int:id>/cancelar/', views.cancelar_reserva, name='cancelar_reserva'),

    # PAGAMENTOS
    path('pagamentos/', views.listar_pagamentos, name='pagamentos'),
    path('pagamentos/cadastrar/', views.cadastrar_pagamento, name='cadastrar_pagamento'),
    path('pagamentos/<int:id>/editar/', views.editar_pagamento, name='editar_pagamento'),
    path('pagamentos/<int:id>/excluir/', views.excluir_pagamento, name='excluir_pagamento'),

]