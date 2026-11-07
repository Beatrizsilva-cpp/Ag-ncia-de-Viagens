
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Destino
from .forms import ClienteForm, DestinoForm


def inicio(request):
    return render(request, 'agencia/inicio.html')


# CLIENTES

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


# DESTINOS

def listar_destinos(request):
    destinos = Destino.objects.all()

    return render(request, 'agencia/destinos.html', {
        'destinos': destinos
    })


def cadastrar_destino(request):
    if request.method == 'POST':
        form = DestinoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('destinos')
    else:
        form = DestinoForm()

    return render(request, 'agencia/cadastrar_destino.html', {
        'form': form
    })


def editar_destino(request, id):
    destino = get_object_or_404(Destino, id=id)

    if request.method == 'POST':
        form = DestinoForm(request.POST, instance=destino)

        if form.is_valid():
            form.save()
            return redirect('destinos')
    else:
        form = DestinoForm(instance=destino)

    return render(request, 'agencia/editar_destino.html', {
        'form': form,
        'destino': destino
    })
    
def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')

    return render(request, 'agencia/excluir_cliente.html', {
        'cliente': cliente
    })
def excluir_destino(request, id):
    destino = get_object_or_404(Destino, id=id)

    if request.method == 'POST':
        if destino.pacotes.exists():
            return render(request, 'agencia/excluir_destino.html', {
                'destino': destino,
                'erro': 'Não é possível excluir este destino, pois existem pacotes de viagem vinculados a ele.'
            })

        destino.delete()
        return redirect('destinos')

    return render(request, 'agencia/excluir_destino.html', {
        'destino': destino
    })
