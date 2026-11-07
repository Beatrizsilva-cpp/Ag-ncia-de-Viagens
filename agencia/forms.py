
from django import forms
from .models import Cliente, Destino, PacoteViagem, Reserva, Pagamento

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'telefone', 'email', 'endereco']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'campo'}),
            'cpf': forms.TextInput(attrs={'class': 'campo'}),
            'telefone': forms.TextInput(attrs={'class': 'campo'}),
            'email': forms.EmailInput(attrs={'class': 'campo'}),
            'endereco': forms.TextInput(attrs={'class': 'campo'}),
        }


class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        fields = ['nome', 'pais', 'estado', 'descricao']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'campo'}),
            'pais': forms.TextInput(attrs={'class': 'campo'}),
            'estado': forms.TextInput(attrs={'class': 'campo'}),
            'descricao': forms.Textarea(attrs={'class': 'campo'}),
        }
        
class PacoteViagemForm(forms.ModelForm):
    class Meta:
        model = PacoteViagem
        fields = [
            'titulo',
            'destino',
            'descricao',
            'data_saida',
            'data_retorno',
            'valor',
            'vagas',
            'ativo'
        ]

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'campo'}),
            'destino': forms.Select(attrs={'class': 'campo'}),
            'descricao': forms.Textarea(attrs={'class': 'campo'}),
            'data_saida': forms.DateInput(
                attrs={'class': 'campo', 'type': 'date'}
            ),
            'data_retorno': forms.DateInput(
                attrs={'class': 'campo', 'type': 'date'}
            ),
            'valor': forms.NumberInput(
                attrs={'class': 'campo', 'step': '0.01'}
            ),
            'vagas': forms.NumberInput(attrs={'class': 'campo'}),
            'ativo': forms.CheckboxInput(),
        }


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            'cliente',
            'pacote',
            'quantidade_pessoas',
            'status'
        ]

        widgets = {
            'cliente': forms.Select(attrs={'class': 'campo'}),
            'pacote': forms.Select(attrs={'class': 'campo'}),
            'quantidade_pessoas': forms.NumberInput(
                attrs={'class': 'campo', 'min': '1'}
            ),
            'status': forms.Select(attrs={'class': 'campo'}),
        }


class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = [
            'reserva',
            'valor',
            'data_pagamento',
            'forma_pagamento',
            'pago'
        ]

        widgets = {
            'reserva': forms.Select(attrs={'class': 'campo'}),
            'valor': forms.NumberInput(
                attrs={'class': 'campo', 'step': '0.01'}
            ),
            'data_pagamento': forms.DateInput(
                attrs={'class': 'campo', 'type': 'date'}
            ),
            'forma_pagamento': forms.Select(
                attrs={'class': 'campo'}
            ),
            'pago': forms.CheckboxInput(),
        }
