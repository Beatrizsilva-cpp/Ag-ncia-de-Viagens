from django import forms
from .models import Cliente


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