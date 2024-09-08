import sys
import os
import unittest



# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from revista import Revista

class TestRevista(unittest.TestCase):
    # TODO Adiciona tus pruebas unitarias aquí.
    # Ejemplo:
    '''
    def test_multiplicar_positivos(self):
        valor_esperado = 15
        mi_cuenta = CuentaBancaria()
        valor_actual = mi_cuenta.multiplicar(3, 5)
        self.assertEqual(valor_esperado, valor_actual)
    '''

    def test_revista(self):
        # Crear una revista con valores específicos
        revista = Revista(125, "Yakelin", "Periferia", 2025)

        # Comprobar que los métodos get devuelven los valores correctos
        self.assertEqual("Periferia", revista.get_titulo())  # Usar el getter heredado
        self.assertEqual(2025, revista.get_ano_publicacion())  # Usar el getter heredado
        self.assertEqual(125, revista.get_numero_revistas())
        self.assertEqual("Yakelin", revista.get_nombre_revista())

        # Comprobar el método __str__()
        expected = "Revista{Titulo=Periferia, anoPublicacion=2025, NumeroRevistas=125, NombreRevista=Yakelin}"
        self.assertEqual(expected, str(revista))

    def test_invalido(self):
        # Probar con valores inválidos, como un año de publicación futuro
        revista_futura = Revista(5, "NombreRevista", "Hola", 2015)
        self.assertEqual(5, revista_futura.get_numero_revistas())
        self.assertEqual(2015, revista_futura.get_ano_publicacion(), "El año de publicación debe ser 2015")

if __name__ == '__main__':
    unittest.main()