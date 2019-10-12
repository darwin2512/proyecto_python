from django.contrib import admin
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import Comunidad, Persona, Actividad, Participante_Actividad

admin.site.register(Comunidad)
admin.site.register(Persona)

class Participante_ActividadInline(admin.TabularInline):
    model = Participante_Actividad

class ActividadAdmin(admin.ModelAdmin):
    inlines = (Participante_ActividadInline,)

admin.site.register(Actividad, ActividadAdmin)

# Register your models here.
