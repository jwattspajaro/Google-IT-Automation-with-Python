from rearrage import rearrange_name  # Importa la función rearrange_name del archivo rearrage.py
import unittest

class TestRearrage(unittest.TestCase):
    def test_basic(self):
        # Prueba básica: nombre en formato "apellido, nombre"
        testcase = 'Lovelace, Ada'
        expected = 'Ada Lovelace'
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        # Prueba con un nombre vacío
        testcase = ''
        expected = ''
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        # Prueba con un nombre que incluye inicial intermedia
        testcase = 'Hopper, Grace M.'
        expected = 'Grace M. Hopper'
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        # Prueba con un solo nombre (sin apellido)
        testcase = 'Voltaire'
        expected = 'Voltaire'
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()  # Ejecuta las pruebas unitarias
