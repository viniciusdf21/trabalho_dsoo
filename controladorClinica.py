from clinica import Clinica
from datetime import time
from telaClinica import TelaClinica

class ControladorClinica:
    def __init__(self):
        self.__clinicas = []
        self.__tela = TelaClinica()

    def cadastrar_clinica(self):
        nome, localizacao, descricao = self.__tela.pegar_dados_clinica()

        while True:
            try:
                ha, ma, hf, mf = self.__tela.pegar_horarios()
                abertura = time(ha, ma)
                fechamento = time(hf, mf)

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

    def excluir_clinica(self):
        nome = input("Nome da clínica que deseja excluir: ")

        for clinica in self.__clinicas:
            if clinica.nome == nome:
                self.__clinicas.remove(clinica)
                print("Clínica removida com sucesso!")
                return

        print("Clínica não encontrada.")
    
    def alterar_clinica(self):
        nome = input("Nome da clínica que deseja alterar: ")

        for clinica in self.__clinicas:
            if clinica.nome == nome:

                clinica.nome = input("Novo nome: ")
                clinica.loc = input("Nova localização: ")
                clinica.descricao = input("Nova descrição: ")

                print("Clínica alterada com sucesso!")
                return

        print("Clínica não encontrada.")

    def escolher_clinica(self):
        if len(self.__clinicas) == 0:
            print("Nenhuma clínica cadastrada.")
            return None

        print("\n=== ESCOLHER CLÍNICA ===")

        for i, clinica in enumerate(self.__clinicas):
            print(f"{i + 1} - {clinica.nome}")

        try:
            opcao = int(input("Escolha a clínica: "))

            if opcao < 1 or opcao > len(self.__clinicas):
                print("Opção inválida.")
                return None

            return self.__clinicas[opcao - 1]

        except ValueError:
            print("Digite um número válido.")
            return None

    def abrir_menu(self):
        while True:

            opcao = self.__tela.mostrar_menu()

            if opcao == "1":
                self.cadastrar_clinica()

            elif opcao == "2":
                self.exibir_clinica()

            elif opcao == "3":
                self.excluir_clinica()

            elif opcao == "4":
                self.alterar_clinica()

            elif opcao == "0":
                break
