from django.contrib import admin
from medicos.models import *

# Register your models here.

class MedicoAdmin(admin.ModelAdmin):
  """
  Admin para o model Medico
  """
  list_display = ['nome', 'crm', 'especialidade', 'telefone', 'areamedica']
  search_fields = ['nome', 'crm']
  list_filter = ['areamedica']

admin.site.register(Medico, MedicoAdmin)
