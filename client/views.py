from django.shortcuts import render, redirect
from client.forms import ClientForm, AddressForm
from client.models import Client, Address, Phone
from django.http import HttpResponse
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
            save_client(request, form)
    else:
        form = ClientForm()
    return {'form': form, 'action': '/client/', 'button': 'Adicionar'}

def save_client(request, form):
    c = Client.objects.create(
        name= form.cleaned_data['name'],
        sex= form.cleaned_data['sex'],
        birthday= form.cleaned_data['birthday'],
        email= form.cleaned_data['email'],
        cpf= form.cleaned_data['cpf'],
        address= form.cleaned_data['address'],
    )
    return index(request=request, message='Cliente cadastrado com sucesso')

@render_to('client/create.html')
def edit_client(request, id):
    c = Client.objects.get(id=id)
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            update_client(request, form, c)
    else:
        form = ClientForm(instance=c)
    return {'form': form, 'action': '/client/edit/'+id+'/', 'button': 'Editar'}

def update_client(request, form, client):
    client.name = form.cleaned_data['name']
    client.sex = form.cleaned_data['sex']
    client.birthday = form.cleaned_data['birthday']
    client.email = form.cleaned_data['email']
    client.cpf = form.cleaned_data['cpf']
    client.address = form.cleaned_data['address']
    client.save()
    return index(request=request, message='Usuario atualizado com sucesso')

def delete_client(request, idP):
    Client.objects.get(id=idP).delete()
    return index(request=request, message='Usuario excluido com sucesso')

@render_to('address/create.html')
def address(request):
    errors = []
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            save_address(form)
        else:
            errors.append('Dados invalidos')
    else:
        form = AddressForm()
    return {'form': form, 'errors': errors, 'action': '/client/'}
    #return render(request, 'address/create.html', {'form': form, 'errors': errors})

def save_address(form):
    a = Address.objects.create(
        street= form.cleaned_data['street'],
        number= form.cleaned_data['number'],
        district= form.cleaned_data['district'],
        zone= form.cleaned_data['zone'],
        city= form.cleaned_data['city'],
    )
    if a:
        # Fazer redirecionamento de volta para pagina de cadstro de cliente
        redirect('http://localhost:8000/client/')
    else:
        return HttpResponse("Fuck")