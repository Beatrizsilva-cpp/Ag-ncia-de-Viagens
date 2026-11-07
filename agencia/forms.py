
from django import forms
from .models import Cliente, Destino


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
