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
def profile(request, idP):
    phone = Phone.objects.filter(client_id=idP)
    return {'client': Client.objects.get(id=idP), 'phone': phone}

@render_to('client/create.html')
def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
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

def delete_client(request, idP):
    Client.objects.get(id=idP).delete()
    return index(request=request, message='Usuario excluido com sucesso')

@render_to('address/create.html')
def address(request):
    errors = []
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/client/')
    else:
        form = AddressForm()
    return {'form': form, 'errors': errors, 'action': '/client/'}