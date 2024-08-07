import unittest
from fatiamento import dividir_altura
from mutatest import Session

class TestDividirAltura(unittest.TestCase):
    def test_dividir_altura(self):
        self.assertEqual(dividir_altura(1.60, 2), 1)  # 1.60m dividido por 3 partes
        self.assertEqual(dividir_altura(1.80, 1), 2)  # 1.80m dividido por 2 partes
        self.assertEqual(dividir_altura(1.50, 4), 1)  # 1.50m dividido por 5 partes
        with self.assertRaises(ValueError):
            dividir_altura(1.60, 0)

if __name__ == '__main__':
    unittest.main()

    session = Session()
    session.run_tests()
