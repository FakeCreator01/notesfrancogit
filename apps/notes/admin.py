from django.contrib import admin
from apps.notes.models import Nota

# Register your models here.

class NotaAdmin(admin.ModelAdmin):
	list_display = ["titulo", "id"]

admin.site.register(Nota, NotaAdmin)