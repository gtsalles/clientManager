from django import forms

class ClientForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    cpf = forms.CharField()
    birthday = forms.DateField()
    sex = forms.ChoiceField(choices=(('M', 'Masculino'), ('F', 'Feminino')))