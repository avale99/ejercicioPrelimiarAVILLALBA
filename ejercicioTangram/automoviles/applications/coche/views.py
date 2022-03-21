from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Coche
from .forms import CocheForm
#api
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from .serializers import CocheSerializer, CocheSerializerBase

#LIST
class ListCochesListView(ListView):
    context_object_name = 'lista_coches'
    template_name = 'coche/lista.html'
    paginate_by = 5

    def get_queryset(self):
        try:
            buscar_clave = self.request.GET.get("busqueda", '')
            if buscar_clave == 'Marca, Modelo, Matricula':
                palabra_clave = self.request.GET.get("kword", '')
                return Coche.objects.listar_coches_kword(palabra_clave)
            elif buscar_clave == 'Fecha inferior a Año-Mes-Dia':
                fecha_clave = self.request.GET.get("kword", '')
                return Coche.objects.listar_coches_ltfecha(fecha_clave)
            else:
                return Coche.objects.all()
        except:
            return Coche.objects.all()

#CREATE
class CocheCreateView(CreateView):
    model = Coche
    template_name = "coche/register.html"
    form_class = CocheForm
    success_url = reverse_lazy('coche_app:list_coches')

    def form_valid(self, form):
        modelo = form.save()
        modelo.save()
        return super(CocheCreateView, self).form_valid(form)

#UPDATE
class CocheUpdateView(UpdateView):
    model = Coche
    template_name = "coche/editar.html"
    fields = [
        'matricula',
        'fecha_creacion',
        'marca',
        'modelo',
    ]
    success_url = reverse_lazy('coche_app:list_coches')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        #request.POST['name']
        return super().post(request, *args, **kwargs)

#DELETE
class CocheDeleteView(DeleteView):
    model = Coche
    template_name = "coche/delete.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = reverse_lazy('coche_app:list_coches')
        self.object.delete()
        return HttpResponseRedirect(success_url)


#API_LIST
class CocheListApiView(ListAPIView):
    serializer_class = CocheSerializer

    def get_queryset(self):
        return Coche.objects.all()

#API_CREATE
class CocheCreateApiView(CreateAPIView):
    serializer_class = CocheSerializerBase

#API_DESTROY
class CocheDestroyApiView(DestroyAPIView):
    serializer_class = CocheSerializer
    queryset = Coche.objects.all()

#API_EDITAR
class CocheUpdateApiView(RetrieveUpdateAPIView):
    serializer_class = CocheSerializerBase
    queryset = Coche.objects.all()

class SelctCochesListView(ListView):
    context_object_name = 'seleccion_coches'
    template_name = 'coche/select_api.html'
    paginate_by = 5

    def get_queryset(self):
        try:
            buscar_clave = self.request.GET.get("busqueda", '')
            if buscar_clave == 'Marca, Modelo, Matricula':
                palabra_clave = self.request.GET.get("kword", '')
                return Coche.objects.listar_coches_kword(palabra_clave)
            elif buscar_clave == 'Fecha inferior a Año-Mes-Dia':
                fecha_clave = self.request.GET.get("kword", '')
                return Coche.objects.listar_coches_ltfecha(fecha_clave)
            else:
                return Coche.objects.all()
        except:
            return Coche.objects.all()

