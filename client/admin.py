from django.contrib import admin
from client.models import *

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'birthday', 'email', 'email', 'cpf', 'address')

admin.site.register(Client)
admin.site.register(Address)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Phone)