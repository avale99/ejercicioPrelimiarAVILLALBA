from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Marca
from .forms import MarcaForm
#api
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from .serializers import MarcaSerializer

class InicioView(TemplateView):
    template_name = 'inicio.html'

# Create your views here.
class ListMarcasListView(ListView):
    context_object_name = 'lista_marcas'
    template_name = 'marca/lista.html'
    paginate_by = 5

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        
        return Marca.objects.listar_marcas(palabra_clave)

class MarcaCreateView(CreateView):
    model = Marca
    template_name = "marca/register.html"
    form_class = MarcaForm
    success_url = reverse_lazy('marca_app:list_marcas')

    def form_valid(self, form):
        marca = form.save()
        marca.save()
        return super(MarcaCreateView, self).form_valid(form)

#UPDATE
class MarcaUpdateView(UpdateView):
    model = Marca
    template_name = "marca/editar.html"
    fields = [
        'nombre',
        'fecha_fundacion',
        'telefono_atencion',
    ]
    success_url = reverse_lazy('marca_app:list_marcas')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        #request.POST['name']
        return super().post(request, *args, **kwargs)

#DELETE
class MarcaDeleteView(DeleteView):
    model = Marca
    template_name = "marca/delete.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = reverse_lazy('marca_app:list_marcas')
        self.object.delete()
        return HttpResponseRedirect(success_url)

#API_LIST
class MarcaListApiView(ListAPIView):
    serializer_class = MarcaSerializer

    def get_queryset(self):
        return Marca.objects.all()

#API_CREATE
class MarcaCreateApiView(CreateAPIView):
    serializer_class = MarcaSerializer

#API_DESTROY
class MarcaDestroyApiView(DestroyAPIView):
    serializer_class = MarcaSerializer
    queryset = Marca.objects.all()

#API_EDITAR
class MarcaUpdateApiView(RetrieveUpdateAPIView):
    serializer_class = MarcaSerializer
    queryset = Marca.objects.all()

class SelectMarcasListView(ListView):
    context_object_name = 'seleccion_marcas'
    template_name = 'marca/select_api.html'
    paginate_by = 5

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        
        return Marca.objects.listar_marcas(palabra_clave)