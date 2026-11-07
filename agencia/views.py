
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Destino, PacoteViagem, Reserva
from .forms import ClienteForm, DestinoForm, PacoteViagemForm, ReservaForm

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
# PACOTES DE VIAGEM

def listar_pacotes(request):
    pacotes = PacoteViagem.objects.select_related('destino').all()

    return render(request, 'agencia/pacotes.html', {
        'pacotes': pacotes
    })


def cadastrar_pacote(request):
    if request.method == 'POST':
        form = PacoteViagemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('pacotes')
    else:
        form = PacoteViagemForm()

    return render(request, 'agencia/cadastrar_pacote.html', {
        'form': form
    })


def editar_pacote(request, id):
    pacote = get_object_or_404(PacoteViagem, id=id)

    if request.method == 'POST':
        form = PacoteViagemForm(request.POST, instance=pacote)

        if form.is_valid():
            form.save()
            return redirect('pacotes')
    else:
        form = PacoteViagemForm(instance=pacote)

    return render(request, 'agencia/editar_pacote.html', {
        'form': form,
        'pacote': pacote
    })


def excluir_pacote(request, id):
    pacote = get_object_or_404(PacoteViagem, id=id)

    if request.method == 'POST':
        if pacote.reservas.exists():
            return render(request, 'agencia/excluir_pacote.html', {
                'pacote': pacote,
                'erro': 'Não é possível excluir este pacote, pois existem reservas vinculadas a ele.'
            })

        pacote.delete()
        return redirect('pacotes')

    return render(request, 'agencia/excluir_pacote.html', {
        'pacote': pacote
    })
    
# RESERVAS

def listar_reservas(request):
    reservas = Reserva.objects.select_related(
        'cliente', 'pacote'
    ).all().order_by('-data_reserva')

    return render(request, 'agencia/reservas.html', {
        'reservas': reservas
    })


def cadastrar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('reservas')
    else:
        form = ReservaForm()

    return render(request, 'agencia/cadastrar_reserva.html', {
        'form': form
    })


def editar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)

    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)

        if form.is_valid():
            form.save()
            return redirect('reservas')
    else:
        form = ReservaForm(instance=reserva)

    return render(request, 'agencia/editar_reserva.html', {
        'form': form,
        'reserva': reserva
    })


def cancelar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)

    if request.method == 'POST':
        reserva.status = 'CANCELADA'
        reserva.save()
        return redirect('reservas')

    return render(request, 'agencia/cancelar_reserva.html', {
        'reserva': reserva
    })
