from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Nota
from .forms import NotaForm
import pywhatkit

# Create your views here.
class Inicio(LoginRequiredMixin, ListView):
	template_name = "notes/inicio.html"
	model = Nota
	queryset = Nota.objects.all()
	context_object_name = "notas"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['notas'] = context['notas'].filter(user=self.request.user)

		# buscador
		busqueda = self.request.GET.get("buscador") #OBTENGO LO QUE SE BUSCO
		if busqueda:
			context['notas'] = context['notas'].filter(titulo__icontains=busqueda)		
		
		return context
		

	#mixins
	login_url = "usuarios/login"
	redirect_field_name = 'usuarios/login.html'

class CrearNota(LoginRequiredMixin, CreateView):
	model = Nota
	form_class = NotaForm
	template_name = "notes/crear_nota.html"
	success_url = reverse_lazy("notas:home")
	context_object_name = "nota"

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(CrearNota, self).form_valid(form)

	#mixins
	login_url = "usuarios/login"
	redirect_field_name = 'usuarios/login.html'


class EditarNota(LoginRequiredMixin, UpdateView):
	template_name = "notes/crear_nota.html"
	model = Nota
	success_url = reverse_lazy("notas:home") # NOTAS (registrado en urls.py src) # HOME (registrado en urls.py de NOTAS)
	form_class = NotaForm

	#mixins
	login_url = "usuarios/login"
	redirect_field_name = 'usuarios/login.html'

class EliminarNota(LoginRequiredMixin, DeleteView):
	model = Nota
	success_url = reverse_lazy("notas:home")
	template_name_suffix = "_eliminar"

	#mixins
	login_url = "usuarios/login"
	redirect_field_name = 'usuarios/login.html'

class VerNota(LoginRequiredMixin, DetailView):
	model = Nota
	template_name = "notes/ver_nota.html"

	#mixins
	login_url = "usuarios/login"
	redirect_field_name = 'usuarios/login.html'