from django.shortcuts import render, redirect
from client.forms import ClientForm, AddressForm
from client.models import Client, Address, Phone
from django.http import HttpResponse
from annoying.decorators import render_to

# CRUD Cliente

@render_to('index.html')
def index(request):
    return {'clients': Client.objects.all()}

@render_to('client/profile.html')
def profile(request, idP):
    phone = Phone.objects.filter(client_id=idP)
    return {'client': Client.objects.get(id=idP), 'phone': phone}

@render_to('client/create.html')
def create_user(request):
    errors = []
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            save_client(form)
        else:
            errors.append('Dados invalidos')
    else:
        form = ClientForm()
    return {'form': form, 'errors': errors}
    #return render(request, 'client/create.html', {'form': form, 'errors': errors})

def save_client(form):
    c = Client.objects.create(
        name= form.cleaned_data['name'],
        sex= form.cleaned_data['sex'],
        birthday= form.cleaned_data['birthday'],
        email= form.cleaned_data['email'],
        cpf= form.cleaned_data['cpf'],
        address= form.cleaned_data['address'],
    )
    if c:
        # Fazer redirecionamento (que funcione) de volta para a index
        return redirect('http://localhost:8000/')

@render_to('client/create.html')
def edit_client(request, idP):
    c = Client.objects.get(id=idP)
    errors = []
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            update_client(form, idP)
        else:
            errors.append('Dados invalidos')
    else:
        form = ClientForm(instance=c)
    return {'form': form, 'errors': errors, 'action': '/update/'+idP}

def update_client(form, idP):
    Client.objects.get(id=idP).update(form.POST)

def delete_client(request, idP):
    Client.objects.get(id=idP).delete()
    return HttpResponse('Usuario excluido com sucesso')

@render_to('address/create.html')
def address(request):
    errors = []
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            save_address(form)
        else:
            errors.append('Dados invalidos')
            return HttpResponse("Fuck1")
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