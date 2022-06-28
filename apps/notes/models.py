from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Nota(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	titulo = models.CharField("Titulo", max_length=50)
	descripcion = models.CharField("Descripcion", max_length=100)
	creado = models.DateTimeField("Creado el", auto_now_add=True)


	def __str__(self):
		return self.titulo
