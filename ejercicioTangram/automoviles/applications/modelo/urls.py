from django.contrib import admin
from django.urls import path
from . import views

app_name = "modelo_app"

urlpatterns = [
    path('lista-modelos/', views.ListModelosListView.as_view(), name="list_modelos"),
    path('registrar-modelo/', views.ModeloCreateView.as_view(), name="regist_modelos"),
    path('editar-modelo/<pk>/', views.ModeloUpdateView.as_view(), name="edit_modelos"),
    path('eliminar-modelo/<pk>/', views.ModeloDeleteView.as_view(), name="delete_modelos"),
    #api
    path('listar-modelos-api/', views.ModeloListApiView.as_view(), name="list_modelos_api"),
    path('registrar-modelo-api/', views.ModeloCreateApiView.as_view(), name="regist_modelos_api"),
    path('eliminar-modelo-api/<pk>/', views.ModeloDestroyApiView.as_view(), name="delete_modelos_api"),
    path('editar-modelo-api/<pk>/', views.ModeloUpdateApiView.as_view(), name="edit_modelos_api"),
    path('select-modelos/', views.SelectModelosListView.as_view(), name="select_modelos"),
]