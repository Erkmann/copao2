from django import forms
from apptimes.models import Usuario

class LoginForm(forms.Form):
    nome_usuario = forms.CharField(label='Nome Usuário', max_length=100)
    senha = forms.CharField(label='senha', max_length=30)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        nome_usuario = cleaned_data.get('nome_usuario')
        senha = cleaned_data.get('email')
        if not nome_usuario and not senha:
            raise forms.ValidationError('You have to write something!')

