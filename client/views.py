from django.shortcuts import render, redirect
from client.forms import ClientForm, AddressForm
from client.models import Client, Address, Phone
from django.http import HttpResponseRedirect
from annoying.decorators import render_to

# CRUD Cliente

@render_to('index.html')
def index(request, message=''):
    return {'clients': Client.objects.all(), 'message': message}

@render_to('client/profile.html')
def profile(request, id):
    return {'client': Client.objects.get(id=id)}

@render_to('client/create.html')
def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            c = form.save()
            c.phone_set.create(number=request.POST['phone'])
            c.save()
            return HttpResponseRedirect('/')
    else:
        form = ClientForm()
    return {'form': form, 'action': '/client/', 'button': 'Adicionar'}

@render_to('client/create.html')
def edit_client(request, id):
    c = Client.objects.get(id=id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=c)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ClientForm(instance=c)
    return {'form': form, 'action': '/client/edit/'+id+'/', 'button': 'Editar'}

def delete_client(request, id):
    Client.objects.get(id=id).delete()
    return index(request=request, message='Usuario excluido com sucesso')

# CRUD Endereco

@render_to('address/create.html')
def address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/client/')
    else:
        form = AddressForm()
    return {'form': form}

@render_to('address/create.html')
def edit_address(request, id):
    a = Address.objects.get(id=id)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/client/')
    else:
        form = AddressForm(instance=a)
    return {'form': form, 'action': '/address/edit/'+id+'/', 'button': 'Editar'}

def delete_address(request, id):
    Address.objects.get(id=id).delete()
    return index(request=request, message='Endereco excluido com sucesso')