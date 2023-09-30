from django.contrib import admin
from django.urls import path
from app_web import views


urlpatterns = [
    path('',views.login,name='inicio_login'),
    path('cadastro/',views.cadastro,name='cadastro_usuario'),
    path('contatos/',views.contato,name='contatos'),
    path('admin/', admin.site.urls),
]
