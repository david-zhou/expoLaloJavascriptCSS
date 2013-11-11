from django import forms
from principal.models import Alumno

class AlumnoForm(forms.ModelForm):
        class Meta:
                model = Alumno
