

from django.test import TestCase
from model_mommy import mommy


# Note que não é preciso importar os modelos, apenas o model_mommy, que chama o modelo como argumento
class ModeloApenasParaTesteTestCase(TestCase):
    def setUp(self):
        self.var = mommy.make('ModeloApenasParaTeste')

    def test_modelo_apenas_para_teste(self):
        self.assertEquals(str(self.var), self.var.texto)  # .texto = campo do modelo [ ModeloApenasParaTeste ]
