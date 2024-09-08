import sys
import os
import unittest

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestLibro(unittest.TestCase):
    # TODO Adiciona tus pruebas unitarias aquí.
    # Ejemplo:
    '''
    def test_multiplicar_positivos(self):
        valor_esperado = 15
        mi_cuenta = CuentaBancaria()
        valor_actual = mi_cuenta.multiplicar(3, 5)
        self.assertEqual(valor_esperado, valor_actual)
    '''
class TestLibro(unittest.TestCase):

    def test_set_titulo(self):
        libro = Libro("Mario", 251, "Amor", 1999)
        self.assertEqual("Mario", libro.get_autor())
        self.assertEqual(1999, libro.get_ano_publicacion())
        self.assertEqual(251, libro.get_numero_de_paginas())

    def test_to_string(self):
        libro = Libro("Harry Potter", 500, "J.K. Rowling", 2024)
        expected = "Libro{Titulo='Harry Potter', Numero_de_paginas=500, Autor='J.K. Rowling', Ano_publicacion=2024}"
        self.assertEqual(expected, str(libro))

    def test_getters(self):
        libro = Libro("Cien años de soledad", 417, "Gabriel García Márquez", 1967)
        self.assertEqual("Cien años de soledad", libro.get_titulo())
        self.assertEqual(417, libro.get_numero_de_paginas())
        self.assertEqual("Gabriel García Márquez", libro.get_autor())
        self.assertEqual(1967, libro.get_ano_publicacion())


if __name__ == '__main__':
    unittest.main()
