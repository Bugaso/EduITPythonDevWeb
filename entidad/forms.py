from django import forms
from django.forms import ModelForm
from .models import Localidad, Persona


# class ClienteForm(forms.Form):
#     nombre = forms.CharField(label="Nombre", max_length=128)
#     edad = forms.IntegerField(label="Edad")
#     activo = forms.BooleanField(label="Activo", required=False)
#     TIPOS_IVA = (
#         (1, "Resp. inscripto"),
#         (2, "Monotributo"),
#         (3, "Exento")
#     )
#     tipo_iva = forms.ChoiceField(label="Tipo Iva", choices=TIPOS_IVA)
#     fecha_nacimiento = forms.DateField(label="Fecha de nacimiento", widget=forms.DateInput(attrs={"type": "date"}))


class LocalidadForm(ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'


class ClienteForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

# REALIZAR TODOS LOS FORMS VINCULADOS CON LOS MODELOS (CLASES DE MODELS)
