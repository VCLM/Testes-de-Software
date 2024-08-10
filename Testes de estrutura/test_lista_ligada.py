# test_lista_ligada.py

import unittest
from lista_ligada import ListaLigada, ListaCircular

class TestListaLigada(unittest.TestCase):
    def test_inserir_fim(self):
        lista = ListaLigada()
        lista.inserir_fim(1)
        lista.inserir_fim(2)
        self.assertEqual(lista.inicio.numero, 1)
        self.assertEqual(lista.inicio.proximo.numero, 2)

    def test_inserir_inicio(self):
        lista = ListaLigada()
        lista.inserir_inicio(1)
        lista.inserir_inicio(2)
        self.assertEqual(lista.inicio.numero, 2)
        self.assertEqual(lista.inicio.proximo.numero, 1)

    def test_inserir_apos(self):
        lista = ListaLigada()
        lista.inserir_fim(1)
        lista.inserir_fim(2)
        lista.inserir_apos(1, 1.5)
        self.assertEqual(lista.inicio.proximo.numero, 1.5)

    def test_delete_no(self):
        lista = ListaLigada()
        lista.inserir_fim(1)
        lista.inserir_fim(2)
        lista.delete_no(1)
        self.assertEqual(lista.inicio.numero, 2)

class TestListaCircular(unittest.TestCase):
    def test_inserir_ordenado(self):
        lista = ListaCircular()
        lista.inserir_ordenado(10)
        lista.inserir_ordenado(5)
        lista.inserir_ordenado(15)
        self.assertEqual(lista.inicio.numero, 5)
        self.assertEqual(lista.inicio.proximo.numero, 10)
        self.assertEqual(lista.inicio.proximo.proximo.numero, 15)

    def test_imprimir_lista(self):
        lista = ListaCircular()
        lista.inserir_ordenado(10)
        lista.inserir_ordenado(5)
        self.assertTrue(lista.inicio.proximo.proximo == lista.inicio)

if __name__ == "__main__":
    unittest.main()
