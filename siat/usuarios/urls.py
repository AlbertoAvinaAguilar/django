from django.urls import path
from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('',views.lista_usuarios, name='lista')
]
