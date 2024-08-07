import math

def dividir_altura(altura, cortes):
    if cortes <= 0:
        raise ValueError("O número de cortes deve ser maior que zero.")
    return math.ceil(altura / (cortes + 1))

# Exemplo de uso
if __name__ == "__main__":
    print(dividir_altura(1.60, 2))  # Deve retornar 1 (1.60 / 3, arredondado para cima)
