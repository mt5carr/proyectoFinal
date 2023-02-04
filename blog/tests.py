import unittest
from blog.models import EntradaDeBlog

class entradaTest(unittest.TestCase):

    def setUp(self):
        self.entradaDeBlog = EntradaDeBlog.objects.create(
            titulo = 'titulo de prueba',
            subtitulo = 'subtitulo de puerba',
            autor = 'matias',
            cuerpo = 'este es el cuerpo del blog, es un texto muyyyy largo....',
        )

    def test_instancia(self):
        """ que se pueda crear la instancia """
        self.assertIsInstance(self.entradaDeBlog, EntradaDeBlog)

    def test_titulo(self):
        """que el título no sea vacío"""
        self.assertIsNotNone(self.entradaDeBlog.titulo)

    def test_subtitulo(self):
        """que el subtítulo no sea vacío"""
        self.assertIsNotNone(self.entradaDeBlog.subtitulo)

