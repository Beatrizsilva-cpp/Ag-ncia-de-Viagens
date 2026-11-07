
from django.contrib import admin
from .models import Cliente, Destino, PacoteViagem, Reserva, Pagamento


admin.site.register(Cliente)
admin.site.register(Destino)
admin.site.register(PacoteViagem)
admin.site.register(Reserva)
admin.site.register(Pagamento)
