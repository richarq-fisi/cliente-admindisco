from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Cliente, Administrador

class ClienteRegistroForm(UserCreationForm):
    telefono = forms.CharField(max_length=15)
    direccion = forms.CharField(max_length=255)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Nombre de usuario"
        self.fields['email'].label = "Correo electrónico"
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"

    field_order = ['username', 'email', 'telefono', 'direccion', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
            Cliente.objects.create(
                user=user, 
                telefono=self.cleaned_data['telefono'], 
                direccion=self.cleaned_data['direccion']
            )
        return user


class AdminRegistroForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    nombre_discoteca = forms.CharField(max_length=255)
    razon_social = forms.CharField(max_length=255)
    ruc = forms.CharField(max_length=11)
    direccion = forms.CharField(max_length=255)
    departamento = forms.CharField(max_length=100)
    provincia = forms.CharField(max_length=100)
    distrito = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=15)
    correo_personal = forms.EmailField(required=False)
    nombre_admin = forms.CharField(max_length=100)

    field_order = ['username',
                    'nombre_admin',
                    'email',
                    'correo_personal',
                    'nombre_discoteca', 
                    'razon_social', 
                    'ruc', 
                    'direccion', 
                    'departamento', 
                    'provincia', 
                    'distrito', 
                    'telefono', 
                    'password1', 
                    'password2'
                    ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admindisco = True
        if commit:
            user.save()
            Administrador.objects.create(
                user=user,
                nombre_discoteca=self.cleaned_data['nombre_discoteca'],
                razon_social=self.cleaned_data['razon_social'],
                ruc=self.cleaned_data['ruc'],
                direccion=self.cleaned_data['direccion'],
                departamento=self.cleaned_data['departamento'],
                provincia=self.cleaned_data['provincia'],
                distrito=self.cleaned_data['distrito'],
                telefono=self.cleaned_data['telefono'],
                correo_personal=self.cleaned_data['correo_personal'],
            )
        return user
