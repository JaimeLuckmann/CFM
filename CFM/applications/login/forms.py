from django import forms
from .models import User
from django.contrib.auth import authenticate
from django import forms
from django.contrib.auth.forms import UserCreationForm


class userRegisterForm(forms.ModelForm):

    password = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput()
    )

    password2 = forms.CharField(
        label="Repetir contraseña",
        required=True,
        widget=forms.PasswordInput()
    )

    class Meta:

        model = User 
        fields = (
            'username',
            'email',
            'nombre',
            'primerApellido',
            )

    # La siguiente función debe tener la palabra clean + "_" + donde 
    # se requiere quese escriba el mensaje en el template. 
    def clean_password2(self):
        """
        Verifica que las dos condiciones sean iguales al crear un usuario.
        """
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            self.add_error('password2','Las contraseñas no son iguales.')

        """
        Verifica que la contraseña tenga al menos 6 dígitos.
        """
        if len(self.cleaned_data['password'])<6:
            self.add_error('password','La contraseña debe tener al menos 6 dígitos.')

"""
Formulario Login.
"""
class LoginForm(forms.Form):

    username = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'fadeIn second mt-2 mb-0',
                'placeholder':'Usuario'
            }
        )
    )

    password = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class':'fadeIn third mb-0 mt-0',
                'placeholder':'Contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm,self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username,password=password):
            raise forms.ValidationError('Los datos del usuario no son correctos')

        return cleaned_data


class UserRegisterForm(UserCreationForm):
    nombre = forms.CharField(max_length=15)
    primerApellido = forms.CharField()
    segundoApellido = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','nombre','primerApellido','segundoApellido', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields }

    primerApellido = forms.CharField(
        label='Primer Apellido',
        required=True,
    )

    segundoApellido = forms.CharField(
        label='Segundo Apellido',
        required=True,
    )

    username = forms.CharField(
        label='Nombre de Usuario',
        required=True,
    )