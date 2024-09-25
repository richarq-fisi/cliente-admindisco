from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Cliente, Administrador

#from django.contrib.auth.models import User

class AdministradorForm(forms.ModelForm):
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    email = forms.EmailField(label="Correo electrónico")
    is_active = forms.BooleanField(label="Cuenta Activa", required=False)  # Campo agregado para is_active

    class Meta:
        model = Administrador
        fields = ['username', 'email', 'nombre_admin', 'nombre_discoteca', 'razon_social', 'ruc', 'direccion', 'departamento', 'provincia', 'distrito', 'telefono', 'correo_personal', 'is_active']

    def __init__(self, *args, **kwargs):
        super(AdministradorForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Inicializamos los campos con los datos del usuario
            self.fields['username'].initial = self.instance.user.username
            self.fields['email'].initial = self.instance.user.email
            self.fields['is_active'].initial = self.instance.user.is_active  # Inicializamos is_active

    def save(self, commit=True):
        # Guardar el administrador sin hacer commit
        administrador = super(AdministradorForm, self).save(commit=False)

        # Guardar el username, email y is_active del usuario relacionado
        user = administrador.user
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.is_active = self.cleaned_data['is_active']  # Guardar el valor de is_active
        user.save()  # Es necesario guardar el usuario explícitamente
        
        # Guardar los demás datos del administrador
        if commit:
            administrador.save()

        return administrador

class ClienteForm(forms.ModelForm):
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    email = forms.EmailField(label="Correo electrónico")
    is_active = forms.BooleanField(label="Cuenta Activa", required=False)  # Campo agregado

    class Meta:
        model = Cliente
        fields = ['username', 'email', 'telefono', 'direccion', 'is_active']  # is_active agregado aquí también

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Inicializamos los campos con los datos del usuario
            self.fields['username'].initial = self.instance.user.username
            self.fields['email'].initial = self.instance.user.email
            self.fields['is_active'].initial = self.instance.user.is_active  # Inicializamos is_active

    def save(self, commit=True):
        # Guardar el cliente sin hacer commit
        cliente = super(ClienteForm, self).save(commit=False)

        # Guardar el username, email y is_active del usuario relacionado
        user = cliente.user
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.is_active = self.cleaned_data['is_active']  # Guardar el valor de is_active
        user.save()  # Es necesario guardar el usuario explícitamente
        
        # Guardar los demás datos del cliente
        if commit:
            cliente.save()

        return cliente

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
        self.fields['username'].widget.attrs.pop('autofocus', None)

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
    # Campos adicionales
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

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # Asegúrate de no añadir autofocus al campo 'username'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Asegura que el campo 'username' no tenga autofocus
        self.fields['username'].widget.attrs.pop('autofocus', None)

    # field_order = ['username',
    #                 'nombre_admin',
    #                 'email',
    #                 'correo_personal',
    #                 'nombre_discoteca', 
    #                 'razon_social', 
    #                 'ruc', 
    #                 'direccion', 
    #                 'departamento', 
    #                 'provincia', 
    #                 'distrito', 
    #                 'telefono', 
    #                 'password1', 
    #                 'password2'
    #                 ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admindisco = True
        if commit:
            user.save()
            Administrador.objects.create(
                user=user,
                nombre_admin=self.cleaned_data['nombre_admin'],
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
                nombre_admin=self.cleaned_data['nombre_admin'], 
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
