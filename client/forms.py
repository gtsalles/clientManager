from django.forms import ModelForm
from client.models import Client, Address

class ClientForm(ModelForm):
    class Meta:
        model = Client

class AddressForm(ModelForm):
    class Meta:
        model = Address