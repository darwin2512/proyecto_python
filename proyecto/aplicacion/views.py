from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from aplicacion.models import Comunidad, Persona, Actividad, Participante_Actividad
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from aplicacion.forms import PersonaForm
from aplicacion.forms import ComunidadForm
from aplicacion.forms import ActividadForm
from aplicacion.forms import ParticipanteActForm
from aplicacion.forms import ParticipanteActFormSet
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator


def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    #num_books = Book.objects.all().count()

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(request,'aplicacion/index.html')


class PersonaListView(generic.ListView):
    model = Persona

class ComunidadListView(generic.ListView):
    model = Comunidad

# ------------------------------------

class ActividadListView(generic.ListView):
    model = Actividad

class ActividadDetailView(generic.DetailView):
    model = Actividad

# ------------------------------------
#CLASES CREATE
    
class PersonaCreate(CreateView):
    model = Persona
    # fields = '__all__'
    form_class = PersonaForm
    success_url = reverse_lazy('aplicacion:personas')
    template_name_suffix = '_crear'

class PersonaUpdate(UpdateView):
    model = Persona
    # fields = ['nombre_persona','apellido','edad','comunidad']
    form_class = PersonaForm
    success_url = reverse_lazy('aplicacion:personas')
    template_name_suffix = '_crear'

class PersonaDelete(DeleteView):
    model = Persona
    success_url = reverse_lazy('aplicacion:personas')
    template_name_suffix = '_eliminar'

    @method_decorator(permission_required('aplicacion.delete_persona',reverse_lazy('aplicacion:personas')))
    def dispatch(self, *args, **kwargs):
        return super(PersonaDelete, self).dispatch(*args, **kwargs)
# ------------------------------------

class ComunidadCreate(CreateView):
    model = Comunidad
    # fields = '__all__'
    form_class = ComunidadForm
    success_url = reverse_lazy('aplicacion:comunidades')
    template_name_suffix = '_crear'

class ComunidadUpdate(UpdateView):
    model = Comunidad
    # fields = ['nombre_comunidad','departamento','municipio']
    form_class = ComunidadForm
    success_url = reverse_lazy('aplicacion:comunidades')
    template_name_suffix = '_crear'

class ComunidadDelete(DeleteView):
    model = Comunidad
    success_url = reverse_lazy('aplicacion:comunidades')
    template_name_suffix = '_eliminar'

    @method_decorator(permission_required('aplicacion.delete_actividad',reverse_lazy('aplicacion:comunidades')))
    def dispatch(self, *args, **kwargs):
        return super(ComunidadDelete, self).dispatch(*args, **kwargs)

# ------------------------------------

class ActividadCreate(CreateView):
    model = Actividad
    # fields = '__all__'
    form_class = ActividadForm
    success_url = reverse_lazy('aplicacion:actividades')
    template_name_suffix = '_crear'

    def get_context_data(self, **kwargs):
        context = super(ActividadCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['actividadespar'] = ParticipanteActFormSet(self.request.POST)
        else:
            context['actividadespar'] = ParticipanteActFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        actividadespar = context['actividadespar']
        if actividadespar.is_valid():
            response = super().form_valid(form)
            actividadespar.instance = self.object
            actividadespar.save()
            return response
        else:           
            return super(ActividadCreate, self).form_valid(form)
    
class ActividadUpdate(UpdateView):
    model = Actividad
    fields = '__all__'
    success_url = reverse_lazy('aplicacion:actividades')
    template_name_suffix = '_crear'

    def get_context_data(self, **kwargs):
        context = super(ActividadUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['actividadespar'] = ParticipanteActFormSet(self.request.POST, instance=self.object)
            context['actividadespar'].full_clean()
        else:
            context['actividadespar'] = ParticipanteActFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        actividadespar = context['actividadespar']
        if actividadespar.is_valid():
            response = super().form_valid(form)
            actividadespar.instance = self.object
            actividadespar.save()
            return response
        else:
            return super(ActividadCreate, self).form_valid(form)

class ActividadDelete(DeleteView):
    model = Actividad
    success_url = reverse_lazy('aplicacion:actividades')
    template_name_suffix = '_eliminar'

    @method_decorator(permission_required('aplicacion.delete_actividad',reverse_lazy('aplicacion:actividades')))
    def dispatch(self, *args, **kwargs):
        return super(ActividadDelete, self).dispatch(*args, **kwargs)