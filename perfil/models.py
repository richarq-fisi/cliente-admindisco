from django.db import models
from django.contrib.auth.models import AbstractUser
from geografia.models import Departamento, Provincia, Distrito
################################################################################

# perfil.User
class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_admindisco = models.BooleanField('admin disco', default=False)
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = "Usuarios"

# perfil.Cliente
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Clientes"

# perfil.Administrador
class Administrador(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_admin = models.CharField(max_length=255)
    nombre_discoteca = models.CharField(max_length=255)
    razon_social = models.CharField(max_length=255)
    ruc = models.CharField(max_length=11, unique=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True)
    distrito = models.ForeignKey(Distrito, on_delete=models.SET_NULL, null=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    correo_personal = models.EmailField(blank=True, null=True)
    class Meta:
        verbose_name_plural = "Administradores de Discoteca"
        
