from django.shortcuts import render_to_response
from client.forms import ClientForm
from django.http import HttpResponse
from django.template import RequestContext, loader

def create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            return HttpResponse("It Worked")
        else:
            return HttpResponse("It did not work")
    else:
        form = ClientForm()
    return render_to_response('client/create.html', {'form': form}, context_instance=RequestContext(request))