# lista_ligada.py

class No:
    def __init__(self, numero):
        self.numero = numero
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.inicio = None

    def inserir_fim(self, numero):
        novo_no = No(numero)
        if self.inicio is None:
            self.inicio = novo_no
            return
        ultimo_no = self.inicio
        while ultimo_no.proximo:
            ultimo_no = ultimo_no.proximo
        ultimo_no.proximo = novo_no

    def inserir_inicio(self, numero):
        novo_no = No(numero)
        novo_no.proximo = self.inicio
        self.inicio = novo_no

    def imprimir_lista(self):
        no_atual = self.inicio
        while no_atual:
            print(no_atual.numero, end=" -> ")
            no_atual = no_atual.proximo
        print("FIM")
    
    def inserir_apos(self, numero, novo_numero):
        no_atual = self.inicio
        while no_atual and no_atual.numero != numero:
            no_atual = no_atual.proximo
        if no_atual is None:
            return False  # Não encontrado
        novo_no = No(novo_numero)
        novo_no.proximo = no_atual.proximo
        no_atual.proximo = novo_no
        return True

    def delete_no(self, numero):
        if self.inicio is None:
            return False  # Lista vazia

        if self.inicio.numero == numero:
            self.inicio = self.inicio.proximo
            return True

        no_anterior = None
        no_atual = self.inicio

        while no_atual and no_atual.numero != numero:
            no_anterior = no_atual
            no_atual = no_atual.proximo

        if no_atual is None:
            return False  # Não encontrado

        no_anterior.proximo = no_atual.proximo
        return True

class ListaCircular:
    def __init__(self):
        self.inicio = None

    def inserir_ordenado(self, numero):
        novo_no = No(numero)

        if self.inicio is None:
            self.inicio = novo_no
            novo_no.proximo = self.inicio
            return

        no_atual = self.inicio
        no_anterior = None

        while True:
            if no_atual.numero >= numero:
                break
            no_anterior = no_atual
            no_atual = no_atual.proximo
            if no_atual == self.inicio:
                break

        if no_anterior is None:  # Inserir no início
            while no_atual.proximo != self.inicio:
                no_atual = no_atual.proximo
            novo_no.proximo = self.inicio
            no_atual.proximo = novo_no
            self.inicio = novo_no
        else:  # Inserir no meio ou no final
            novo_no.proximo = no_atual
            no_anterior.proximo = novo_no

    def imprimir_lista(self):
        if self.inicio is None:
            print("FIM")
            return

        no_atual = self.inicio
        while True:
            print(no_atual.numero, end=" -> ")
            no_atual = no_atual.proximo
            if no_atual == self.inicio:
                break
        print("INÍCIO")
