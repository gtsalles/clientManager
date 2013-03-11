from django.db import models
from serializers import ModelSerializer

class Client(models.Model):
    name = models.CharField('Nome', max_length=100)
    sex = models.CharField('Sexo', max_length=1, choices=(('M', 'Masculino'), ('F', 'Feminino')))
    birthday = models.DateField('Data de Nascimento')
    email = models.EmailField('Email')
    cpf = models.CharField('CPF', max_length=11)
    address = models.ForeignKey('Address', verbose_name='Endereco')
    indicator = models.ForeignKey('Client', blank=True, null=True, verbose_name='Quem o indicou?')

    def get_phones(self):
        p = [pp.number for pp in self.phone_set.all()]
        return u', '.join(p)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Address(models.Model):
    street = models.CharField('Rua', max_length=50)
    number = models.IntegerField('Numero')
    district = models.CharField('Bairro', max_length=50)
    zone = models.CharField('Zona', max_length=50)
    city = models.ForeignKey('City', verbose_name='Cidade')

    def __unicode__(self):
        return u'%s %s, %s, %s - %s' % (self.street, self.number, self.district, self.city, self.city.state)

    class Meta:
        ordering = ['street', 'number']

class City(models.Model):
    name = models.CharField('Nome', max_length=50)
    state = models.ForeignKey('State', verbose_name='Estado')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class State(models.Model):
    name = models.CharField('Nome', max_length=50)
    acr = models.CharField('Sigla', max_length=2)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Phone(models.Model):
    number = models.CharField('Numero', max_length=11)
    client = models.ForeignKey('Client')

    def __unicode__(self):
        return self.number

    class Meta:
        ordering = ['number']

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client