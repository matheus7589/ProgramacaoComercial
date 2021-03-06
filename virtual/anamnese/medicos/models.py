from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Medico(models.Model):
  nome = models.CharField(max_length=100)
  crm = models.IntegerField()
  especialidade = models.CharField(max_length=100)
  telefone = models.IntegerField()
  areamedica = models.SmallIntegerField(choices=[(1, 'INFECTOLOGISTA'), (2, 'CLINICA MEDICA'), (3, 'MEDICINA DE FAMILIA E COMUNIDADE')])

  def __str__(self):
    return '{0} - {1} ({2}/{3})'.format(self.nome, self.crm, self.especialidade, self.telefone, self.areamedica)
