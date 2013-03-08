from django.contrib import admin
from client.models import *

admin.site.register(Client)
admin.site.register(Address)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Phone)