from client.forms import ClientForm, AddressForm
from client.models import Client, Address, ClientSerializer
from django.http import HttpResponseRedirect, HttpResponse
from annoying.decorators import render_to
import csv
from django.template.defaultfilters import slugify

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
    return {'form': form, 'button': 'Criar'}

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

# Tentando exportar os dados

def teste(request):
    export(Client.objects.all())
#    serializer = ClientSerializer()
#    stream = serializer.serialize('csv', Client.objects.all(), indent=4)
#
#
#    response = HttpResponse(content_type='text/csv')
#    response['Content-Disposition'] = 'attachment; filename="clientes.csv"'
#    writer = csv.writer(response)
#
#    f = file('clientes.csv', 'w')
#    f.write(stream)
#    f.close()
#
#    writer.writerow(f)
#
#    return response
    #writer = csv.writer(response)
    #writer.writerow(stream)
    #return response



#    export(Client.objects.all().model)


    #export(Client.objects.all())
    #exporter.export(request, c, 'Client', 'Clients')

#
#    response = HttpResponse(content_type='text/csv')
#    response['Content-Disposition'] = 'attachment; filename="teste.csv"'
#    writer = csv.writer(response)
#
#    c = Client.objects.all()
#
#    writer.writerow(['Nome Sexo Data_Nascimento Email CPF Endereco'])
#    row = []
#    for client in c:
#        #row.append([client.name, client.sex, client.address, client.birthday, client.email, client.cpf, client.address])
#        row.append([client.name])
#        writer.writerow(row)
#
#    return response


# Erro na hora de ler as strings ('ascii' codec can't encode character u'\xf4' in position 3:)

#def export(qs, fields=None):
#    model = qs.model
#    response = HttpResponse(mimetype='text/csv')
#    response['Content-Disposition'] = 'attachment; filename=%s.csv' % slugify(model.__name__)
#    writer = csv.writer(response)
#    # Write headers to CSV file
#    if fields:
#        headers = fields
#    else:
#        headers = []
#        for field in model._meta.fields:
#            headers.append(field.name)
#    writer.writerow(headers)
#    # Write data to CSV file
#    for obj in qs:
#        row = []
#        for field in headers:
#            if field in headers:
#                val = getattr(obj, field)
#                if callable(val):
#                    val = val()
#                row.append(val)
#        writer.writerow(row)
#        # Return CSV file to browser as download
#    return response

#'QuerySet' object has no attribute 'META'
#def export(model):
#    response = HttpResponse(mimetype='text/csv')
#    response['Content-Disposition'] = 'attachment; filename=%s.csv' #% slugify(model.__name__)
#    writer = csv.writer(response)
#    # Write headers to CSV file
#    headers = []
#    for field in model._meta.fields:
#        headers.append(field.name)
#    writer.writerow(headers)
#    # Write data to CSV file
#    print model.objects.all()
#    for obj in model.objects.all().order_by("id"):
#        row = []
#        for field in model._meta.fields:
#            row.append(getattr(obj, field.name))
#        writer.writerow(row)
#        # Return CSV file to browser as download
#    return response