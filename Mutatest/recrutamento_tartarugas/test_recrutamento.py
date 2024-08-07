import unittest
from recrutamento import Tartaruga, RecrutamentoTartarugas
from mutatest import Session

class TestRecrutamentoTartarugas(unittest.TestCase):
    def setUp(self):
        self.tartarugas = [
            Tartaruga("Ninja1", 16, "Espada", 50),
            Tartaruga("Ninja2", 22, "Bumerangue", 70),
            Tartaruga("Ninja3", 25, "Nunchaku", 40),
            Tartaruga("Ninja4", 19, "Shuriken", 35),
            Tartaruga("Leonardo", 20, "Katana", 60),
            Tartaruga("Ninja5", 14, "Arco", 55),
            Tartaruga("Ninja6", 31, "Machado", 50),
            Tartaruga("Ninja7", 18, "Estrela", 90)
        ]

    def test_tartaruga_qualificada(self):
        self.assertFalse(RecrutamentoTartarugas.tartaruga_qualificada(self.tartarugas[0])) # Nome repetido
        self.assertTrue(RecrutamentoTartarugas.tartaruga_qualificada(self.tartarugas[1]))  # Qualificada
        self.assertFalse(RecrutamentoTartarugas.tartaruga_qualificada(self.tartarugas[2])) # Arma repetida
        self.assertTrue(RecrutamentoTartarugas.tartaruga_qualificada(self.tartarugas[3]))  # Qualificada
        self.assertFalse(RecrutamentoTartarugas.tartaruga_qualificada(self.tartarugas[4])) # Nome repetido
        self.assertFalse(RecrutamentoTartarugas.tartaruga_qualificada(self.tartarugas[5])) # Idade fora do intervalo
        self.assertFalse(RecrutamentoTartarugas.tartaruga_qualificada(self.tartarugas[6])) # Idade fora do intervalo
        self.assertFalse(RecrutamentoTartarugas.tartaruga_qualificada(self.tartarugas[7])) # Radiação fora do intervalo

if __name__ == '__main__':
    unittest.main()

    session = Session()
    session.run_tests()
