from django.test import TestCase
from aluraflix.models import Programa

class ProgramaModelTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo = 'Procurando ninguém em latim',
            data_lancamento = '2003-07-04'
        )

        def test_verifica_atributos_do_programa(self):
            """Teste que verifica os atributos os atributos de um program com os valores default"""
            self.asserEqual(self.programa.titulo, 'Procurando ninguém em latim')
            self.asserEqual(self.programa.tipo, 'F')
            self.asserEqual(self.programa.data_lancamento, '2003-07-04')
            self.asserEqual(self.programa.likes, '0')
            self.asserEqual(self.programa.dislikes, '0')