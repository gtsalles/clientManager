from django.shortcuts import render_to_response
from client.forms import ClientForm
from django.http import HttpResponse

def create_form(request):
    return render_to_response('client/create.html', {'form': ClientForm()})

def create(request):
    form = ClientForm(request.POST)
    if form.is_valid():
        return HttpResponse("It Worked")
    return HttpResponse("It didn't worked")