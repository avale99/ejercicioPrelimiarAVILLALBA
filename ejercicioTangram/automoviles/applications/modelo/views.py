from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Modelo
from .forms import ModeloForm
#api
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from .serializers import ModeloSerializer

#LIST
class ListModelosListView(ListView):
    context_object_name = 'lista_modelos'
    template_name = 'modelo/lista.html'
    paginate_by = 5

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        return Modelo.objects.listar_modelos(palabra_clave)

#REGISTER
class ModeloCreateView(CreateView):
    model = Modelo
    template_name = "modelo/register.html"
    form_class = ModeloForm
    success_url = reverse_lazy('modelo_app:list_modelos')

    def form_valid(self, form):
        modelo = form.save()
        modelo.save()
        return super(ModeloCreateView, self).form_valid(form)

#UPDATE
class ModeloUpdateView(UpdateView):
    model = Modelo
    template_name = "modelo/editar.html"
    fields = [
        'nombre',
        'carroceria',
    ]
    success_url = reverse_lazy('modelo_app:list_modelos')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        #request.POST['name']
        return super().post(request, *args, **kwargs)

#DELETE
class ModeloDeleteView(DeleteView):
    model = Modelo
    template_name = "modelo/delete.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = reverse_lazy('modelo_app:list_modelos')
        self.object.delete()
        return HttpResponseRedirect(success_url)

#API_LIST
class ModeloListApiView(ListAPIView):
    serializer_class = ModeloSerializer

    def get_queryset(self):
        return Modelo.objects.all()

#API_CREATE
class ModeloCreateApiView(CreateAPIView):
    serializer_class = ModeloSerializer

#API_DESTROY
class ModeloDestroyApiView(DestroyAPIView):
    serializer_class = ModeloSerializer
    queryset = Modelo.objects.all()

#API_EDITAR
class ModeloUpdateApiView(RetrieveUpdateAPIView):
    serializer_class = ModeloSerializer
    queryset = Modelo.objects.all()

class SelectModelosListView(ListView):
    context_object_name = 'seleccion_modelos'
    template_name = 'modelo/select_api.html'
    paginate_by = 5

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        return Modelo.objects.listar_modelos(palabra_clave)


