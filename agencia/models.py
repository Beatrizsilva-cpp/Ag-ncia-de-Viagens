
from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Destino(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class PacoteViagem(models.Model):
    titulo = models.CharField(max_length=150)
    destino = models.ForeignKey(
        Destino,
        on_delete=models.PROTECT,
        related_name="pacotes"
    )
    descricao = models.TextField()
    data_saida = models.DateField()
    data_retorno = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    vagas = models.PositiveIntegerField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Reserva(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('CONFIRMADA', 'Confirmada'),
        ('CANCELADA', 'Cancelada'),
    ]

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name="reservas"
    )
    pacote = models.ForeignKey(
        PacoteViagem,
        on_delete=models.PROTECT,
        related_name="reservas"
    )
    data_reserva = models.DateTimeField(auto_now_add=True)
    quantidade_pessoas = models.PositiveIntegerField(default=1)
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='PENDENTE'
    )

    def __str__(self):
        return f"Reserva {self.id} - {self.cliente.nome}"


class Pagamento(models.Model):
    FORMA_CHOICES = [
        ('PIX', 'Pix'),
        ('CARTAO', 'Cartão'),
        ('DINHEIRO', 'Dinheiro'),
        ('TRANSFERENCIA', 'Transferência'),
    ]

    reserva = models.ForeignKey(
        Reserva,
        on_delete=models.PROTECT,
        related_name="pagamentos"
    )
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField()
    forma_pagamento = models.CharField(
        max_length=20,
        choices=FORMA_CHOICES
    )
    pago = models.BooleanField(default=False)

    def __str__(self):
        return f"Pagamento {self.id} - Reserva {self.reserva.id}"
