from django.shortcuts import render
from client.forms import ClientForm, AddressForm
from client.models import Client, Address
from django.http import HttpResponseRedirect, HttpResponse

def create(request):
    errors = []
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            save_client(form)
        else:
            errors.append('Dados invalidos')
    else:
        form = ClientForm()
    return render(request, 'client/create.html', {'form': form, 'errors': errors})

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
        return HttpResponseRedirect('http://localhost:8000/')

def index(request):
    clients = Client.objects.all()
    return render(request, 'index.html', {'clients': clients})

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
    return render(request, 'address/create.html', {'form': form, 'errors': errors})

def save_address(form):
    a = Address.objects.create(
        street= form.cleaned_data['street'],
        number= form.cleaned_data['number'],
        district= form.cleaned_data['district'],
        zone= form.cleaned_data['zone'],
        city= form.cleaned_data['city'],
    )
    if a:
        return HttpResponseRedirect('http://localhost:8000/address/')
    else:
        return HttpResponse("Fuck")