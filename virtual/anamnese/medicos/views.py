# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from medicos.forms import *
from medicos.models import *

class MedicosList(ListView):
  """
  View para listar médicos cadastrados.
  """
  model = Medico
  template_name = 'medicos/listar.html'

class MedicosNew(CreateView):
  """
  View para a criação de novos médicos.
  """
  model = Medico
  form_class = FormularioMedico
  template_name = 'medicos/novo.html'
  success_url = reverse_lazy('listar-medicos')

class MedicosEdit(UpdateView):
  """
  View para a edição de médicos já cadastrados.
  """
  model = Medico
  form_class = FormularioMedico
  template_name = 'medicos/editar.html'
  success_url = reverse_lazy('listar-medicos')

class MedicosDelete(DeleteView):
  """
  View para a exclusão de médicos.
  """
  model = Medico
  template_name = 'medicos/deletar.html'
  success_url = reverse_lazy('listar-medicos')
