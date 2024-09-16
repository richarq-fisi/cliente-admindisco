from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views
from django.conf.urls import handler404
from .views import page_not_found

handler404 = page_not_found

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('registro/cliente/', views.cliente_registro, name='cliente_registro'),
    path('registro/administrador/', views.administrador_registro, name='admin_registro'),
    path('login/', views.login_view, name='login'),
    path('cliente_panel/', views.cliente_panel, name='cliente_panel'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]

