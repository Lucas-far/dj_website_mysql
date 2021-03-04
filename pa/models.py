

from django.db import models


# ------------------------------------- modelo de exemplo para testar [ coverage ] -------------------------------------
class ModeloApenasParaTeste(models.Model):
    texto = models.CharField('Texto', max_length=500)

    class Meta:
        verbose_name = 'Texto'
        verbose_name_plural = 'Textos'

    def __str__(self):
        return self.texto
