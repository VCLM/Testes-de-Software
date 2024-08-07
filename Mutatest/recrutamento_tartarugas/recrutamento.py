class Tartaruga:
    def __init__(self, nome, idade, arma, nivel_radiacao):
        self.nome = nome
        self.idade = idade
        self.arma = arma
        self.nivel_radiacao = nivel_radiacao

class RecrutamentoTartarugas:
    equipe_original = ["Leonardo", "Michelangelo", "Donatello", "Raphael"]
    armas_original = ["Espada", "Nunchaku", "Bastão", "Sai"]

    @staticmethod
    def tartaruga_qualificada(tartaruga):
        if tartaruga.nome in RecrutamentoTartarugas.equipe_original:
            return False
        if tartaruga.arma in RecrutamentoTartarugas.armas_original:
            return False
        if not (15 <= tartaruga.idade <= 30):
            return False
        if not (30 <= tartaruga.nivel_radiacao <= 80):
            return False
        return True

# Exemplo de uso
if __name__ == "__main__":
    novas_tartarugas = [
        Tartaruga("Ninja1", 16, "Espada", 50),
        Tartaruga("Ninja2", 22, "Bumerangue", 70),
        Tartaruga("Ninja3", 25, "Nunchaku", 40),
        Tartaruga("Ninja4", 19, "Shuriken", 35)
    ]

    for tartaruga in novas_tartarugas:
        if RecrutamentoTartarugas.tartaruga_qualificada(tartaruga):
            print(f"{tartaruga.nome} está qualificada.")
        else:
            print(f"{tartaruga.nome} não está qualificada.")