from django.db import models

class Client(models.Model):
    name = models.CharField('Nome', max_length=100)
    sex = models.CharField('Sexo', max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    birthday = models.DateField()
    email = models.EmailField()
    cpf = models.CharField('CPF', max_length=11)
    address = models.ForeignKey('Address')
    phone = models.ForeignKey('Phone')

class Address(models.Model):
    street = models.CharField('Rua', max_length=50)
    number = models.IntegerField()
    neighborhood = models.CharField('Bairro', max_length=50)
    zone = models.CharField('Zona', max_length=50)
    city = models.ForeignKey('City')

class City(models.Model):
    name = models.CharField('Nome', max_length=50)
    state = models.ForeignKey('State')

class State(models.Model):
    name = models.CharField('Nome', max_length=50)
    acr = models.CharField('Sigla', max_length=2)

class Phone(models.Model):
    number = models.CharField('numero', max_length=11)