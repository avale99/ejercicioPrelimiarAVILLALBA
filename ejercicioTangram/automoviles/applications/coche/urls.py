from django.contrib import admin
from django.urls import path
from . import views

app_name = "coche_app"

urlpatterns = [
    path('lista-coches/', views.ListCochesListView.as_view(), name="list_coches"),
    path('registrar-coche/', views.CocheCreateView.as_view(), name="regist_coches"),
    path('editar-coche/<pk>/', views.CocheUpdateView.as_view(), name="edit_coches"),
    path('eliminar-coche/<pk>/', views.CocheDeleteView.as_view(), name="delete_coches"),
    #api
    path('listar-coches-api/', views.CocheListApiView.as_view(), name="list_coches_api"),
    path('registrar-coche-api/', views.CocheCreateApiView.as_view(), name="regist_coches_api"),
    path('eliminar-coche-api/<pk>/', views.CocheDestroyApiView.as_view(), name="delete_coches_api"),
    path('editar-coche-api/<pk>/', views.CocheUpdateApiView.as_view(), name="edit_coches_api"),
    path('select-coches/', views.SelctCochesListView.as_view(), name="select_coches"),
]