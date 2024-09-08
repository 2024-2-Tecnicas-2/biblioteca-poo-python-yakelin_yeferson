import sys
import os
import unittest


# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from publicacion import Publicacion

class TestPublicacion(unittest.TestCase):
    # TODO Adiciona tus pruebas unitarias aquí.
    # Ejemplo:
    '''
    def test_multiplicar_positivos(self):
        valor_esperado = 15
        mi_cuenta = CuentaBancaria()
        valor_actual = mi_cuenta.multiplicar(3, 5)
        self.assertEqual(valor_esperado, valor_actual)
    '''
    def test_set_titulo(self):
        publicacion = Publicacion()
        publicacion.set_titulo("Jeferson Bobis")
        self.assertEqual("Jeferson Bobis", publicacion.get_titulo())

    def test_set_ano_publicacion(self):
        publicacion = Publicacion()
        publicacion.set_ano_publicacion(2023)
        self.assertEqual(2023, publicacion.get_ano_publicacion())

if __name__ == '__main__':
    unittest.main()
