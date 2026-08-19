import unittest

from gerenciador_notas import calcular_media, verificar_aprovacao


class TestNotas(unittest.TestCase):
    """Testes de validação para o núcleo acadêmico."""

    def test_aprovacao_com_media_normal(self):
        """Verifica aprovação com notas comuns acima da média mínima."""
        notas = [8.0, 7.0, 9.0]
        media = calcular_media(notas)

        self.assertEqual(media, 8.0)
        self.assertTrue(verificar_aprovacao(media, 7.0))

    def test_reprovacao_com_media_normal(self):
        """Verifica reprovação com notas comuns abaixo da média mínima."""
        notas = [5.0, 6.0, 4.0]
        media = calcular_media(notas)

        self.assertEqual(media, 5.0)
        self.assertFalse(verificar_aprovacao(media, 7.0))

    def test_lista_de_notas_vazia(self):
        """Verifica o comportamento da média com lista vazia."""
        notas = []
        media = calcular_media(notas)

        self.assertEqual(media, 0)

    def test_media_minima_zero(self):
        """Verifica aprovação quando a média mínima é zero."""
        notas = [0.0, 0.0, 0.0]
        media = calcular_media(notas)

        self.assertEqual(media, 0.0)
        self.assertTrue(verificar_aprovacao(media, 0))


if __name__ == "__main__":
    unittest.main()
