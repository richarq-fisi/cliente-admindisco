from django.contrib import admin
from .models import User, Cliente, Administrador

# MODELO USUARIO
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_superuser')
    search_fields = ['username']

# MODELO ADMINISTRADOR DISCOTECA
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_email', 'get_is_active')

    def get_username(self, obj):
        return obj.user.username
    def get_email(self, obj):
        return obj.user.email
    def get_is_active(self, obj):
        return obj.user.is_active

    get_username.short_description = 'Usuario admin discoteca'
    get_email.short_description = 'Email'
    get_is_active.boolean = True
    get_is_active.short_description = 'Cuenta Activa'

# MODELO CLIENTE
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_email', 'get_is_active')

    def get_username(self, obj):
        return obj.user.username  # Accede al username de User  
    def get_email(self, obj):
        return obj.user.email  # Accede al email de User
    def get_is_active(self, obj):
        return obj.user.is_active  # Accede al estado is_active de User

    get_username.short_description = 'Usuario cliente'
    get_email.short_description = 'Email'
    get_is_active.boolean = True
    get_is_active.short_description = 'Cuenta Activa'

# REGISTRO DE MODELOS
admin.site.register(User, UserAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Administrador, AdministradorAdmin)

