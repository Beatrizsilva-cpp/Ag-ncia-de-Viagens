from django.shortcuts import render, redirect, get_object_or_404
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


def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'agencia/editar_cliente.html', {
        'form': form,
        'cliente': cliente
    })


def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')

    return render(request, 'agencia/excluir_cliente.html', {
        'cliente': cliente
    })