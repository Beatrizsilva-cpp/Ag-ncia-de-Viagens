from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm


def inicio(request):
    return render(request, 'agencia/inicio.html')


def listar_clientes(request):
    clientes = Cliente.objects.all()

    return render(request, 'agencia/clientes.html', {
        'clientes': clientes
    })


def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()

    return render(request, 'agencia/cadastrar_cliente.html', {
        'form': form
    })