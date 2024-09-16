from django.contrib import admin
from .models import User, Cliente, Administrador
from django.contrib.auth.models import Group

# Desregistrar el modelo 'Group'
admin.site.unregister(Group)

# MODELO USUARIO
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_superuser')
    search_fields = ['username']

# MODELO ADMINISTRADOR DISCOTECA
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_email', 'get_is_active', 'get_date_joined')

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
class ClienteAdmin(admin.ModelAdmin):
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

# REGISTRO DE MODELOS
admin.site.register(User, UserAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Administrador, AdministradorAdmin)

