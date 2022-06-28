from django import forms
from .models import Nota

class NotaForm(forms.ModelForm):
	class Meta:
		# a que modelo hace referencia
		model = Nota
		# que campos muestra
		fields = ["titulo", "descripcion"]