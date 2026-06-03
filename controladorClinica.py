from clinica import Clinica
from datetime import time


class ControladorClinica:
    def __init__(self):
        self.__clinica = []

    def cadastrar_clinica(self):
        nome = input("Nome: ")
        localizacao = input("Localização: ")
        descricao = input("Descrição: ")

        abertura = time(
            int(input("Hora abertura: ")),
            int(input("Minuto abertura: "))
        )

        fechamento = time(
            int(input("Hora fechamento: ")),
            int(input("Minuto fechamento: "))
        )

        self.__clinica = Clinica(nome, loc, descricao, abertura, fechamento)

    def exibir_clinica(self):
        if self.__clinica:
            print(self.__clinica.exibir_dados())
        else:
            print("Nenhuma clínica cadastrada.")

    def abrir_menu(self):
        while True:
            print("\n=== CLÍNICA ===")
            print("1 - Cadastrar")
            print("2 - Exibir")
            print("0 - Voltar")

            opcao = input("Opção: ")

            if opcao == "1":
                self.cadastrar_clinica()

            elif opcao == "2":
                self.exibir_clinica()

            elif opcao == "0":
                break
