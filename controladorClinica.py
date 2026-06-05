from clinica import Clinica
from datetime import time


class ControladorClinica:
    def __init__(self):
        self.__clinicas = []

    def cadastrar_clinica(self):
        nome = input("Nome: ")
        localizacao = input("Localização: ")
        descricao = input("Descrição: ")

        while True:
            try:
                abertura = time(
                    int(input("Hora abertura: ")),
                    int(input("Minuto abertura: "))
                )
        
                fechamento = time(
                    int(input("Hora fechamento: ")),
                    int(input("Minuto fechamento: "))
                )

                clinica = Clinica(nome, localizacao, descricao, abertura, fechamento)
                self.__clinicas.append(clinica)
                print("Clínica cadastrada com sucesso!")
                break
            
            except ValueError:
                print("Horário inválido. Tente novamente.")
    
    def exibir_clinica(self):
        if not self.__clinicas:
            print("Nenhuma clínica cadastrada.")
            return

        for clinica in self.__clinicas:
            print("\n")
            print(clinica.exibir_dados())

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
