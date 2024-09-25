from django.contrib import admin
from .models import User, Cliente, Administrador
from django.contrib.auth.models import Group
from django.contrib.admin import SimpleListFilter
from unfold.admin import ModelAdmin
#from django.contrib.admin import ModelAdmin
from .forms import ClienteForm, AdministradorForm

# Desregistrar el modelo 'Group'
admin.site.unregister(Group)

# Filtro personalizado para 'Cuenta Activa'
class CuentaActivaFilter(SimpleListFilter):
    title = 'Cuenta_Activa'  # Nombre que se mostrará en la interfaz de administración
    parameter_name = 'user_is_active'  # Parámetro que se usa en la URL para el filtro

    def lookups(self, request, model_admin):
        return (
            ('1', 'Activo'),
            ('0', 'Inactivo'),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.filter(user__is_active=True)
        if self.value() == '0':
            return queryset.filter(user__is_active=False)

class CuentaUserFilter(SimpleListFilter):
    title = 'Cuenta_Usuario'
    parameter_name = 'is_admindisco'

    def lookups(self, request, model_admin):
        return (
            ('1', 'AdminDiscoteca'),
            ('0', 'Cliente'),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.filter(is_admindisco=True)
        if self.value() == '0':
            return queryset.filter(is_admindisco=False)

# MODELO USUARIO
class UserAdmin(ModelAdmin):
    list_display = ('username', 'email', 'get_is_active')
    search_fields = ['username']
    list_filter = (CuentaUserFilter,)

    def get_is_active(self, obj):
        return obj.is_active

    get_is_active.boolean = True
    get_is_active.short_description = 'Cuenta Activa'

# MODELO ADMINISTRADOR DISCOTECA
class AdministradorAdmin(ModelAdmin):
    form = AdministradorForm
    list_display = ('get_username', 'get_email', 'get_is_active', 'get_date_joined')
    list_filter = (CuentaActivaFilter,)  # Filtro personalizado agregado aquí

    def get_username(self, obj):
        return obj.user.username
    def get_email(self, obj):
        return obj.user.email
    def get_is_active(self, obj):
        return obj.user.is_active
    def get_date_joined(self, obj):
        return obj.user.date_joined

    get_username.short_description = 'Usuario admin discoteca'
    get_email.short_description = 'Email'
    get_is_active.boolean = True
    get_is_active.short_description = 'Cuenta Activa'
    get_date_joined.short_description = 'Fecha Registro'

# MODELO CLIENTE
class ClienteAdmin(ModelAdmin):
    form = ClienteForm  # Utilizar el nuevo formulario personalizado
    list_display = ('get_username', 'get_email', 'get_is_active', 'get_date_joined')

    def get_username(self, obj):
        return obj.user.username  # Accede al username de User  
    def get_email(self, obj):
        return obj.user.email  # Accede al email de User
    def get_is_active(self, obj):
        return obj.user.is_active  # Accede al estado is_active de User
    def get_date_joined(self, obj):
        return obj.user.date_joined

    get_username.short_description = 'Usuario cliente'
    get_email.short_description = 'Email'
    get_is_active.boolean = True
    get_is_active.short_description = 'Cuenta Activa'
    get_date_joined.short_description = 'Fecha Registro'

class UserAdmin(ModelAdmin):
    list_display = ('username', 'email', 'get_is_active')
    search_fields = ['username']
    list_filter = (CuentaUserFilter,)

    def get_is_active(self, obj):
        return obj.is_active

    get_is_active.boolean = True
    get_is_active.short_description = 'Cuenta Activa'

# REGISTRO DE MODELOS
admin.site.register(User, UserAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Administrador, AdministradorAdmin)
