from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import Comunidad, Persona, Actividad, Participante_Actividad
from django.forms import SelectDateWidget
from django.utils import timezone, timesince

class ActividadForm(ModelForm):

    class Meta:

        model = Actividad
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})
        }

class PersonaForm(ModelForm):

    def __init__(self, *args, **kwargs):
            super(PersonaForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
                'nombre': forms.TextInput(attrs={'class': 'input', 'autofocus': True}),
            }

class ComunidadForm(ModelForm):

    def __init__(self, *args, **kwargs):
            super(ComunidadForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Comunidad
        fields = '__all__'
         
    

class ParticipanteActForm(ModelForm):
    persona = forms.ModelChoiceField(queryset=Persona.objects.all(),empty_label="Seleccione un Participante")

    class Meta:
        model = Participante_Actividad
        exclude = ()

ParticipanteActFormSet = inlineformset_factory(Actividad, Participante_Actividad, form=ParticipanteActForm, extra=5, can_delete=True)
