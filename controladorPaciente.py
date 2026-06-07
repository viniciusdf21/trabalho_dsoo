from paciente import Paciente
from datetime import date
from telaPaciente import TelaPaciente


class ControladorPaciente:
    def __init__(self):
        self.__pacientes = []
        self.__tela = TelaPaciente()

    def cadastrar_paciente(self):
        nome, cpf, celular = self.__tela.pegar_dados_paciente()

        while True:
            try:
                ano, mes, dia = self.__tela.pegar_data_nascimento()
        
                data_nascimento = date(ano, mes, dia)
                break

            except ValueError: 
                print("Data inválida. Tente Novamente.") 

        try:
            paciente = Paciente(nome, cpf, celular, data_nascimento)
            self.__pacientes.append(paciente)
            print("Paciente cadastrado com sucesso!")

        except ValueError as erro:
            print(erro)

    def listar_pacientes(self):
        self.__tela.mostrar_pacientes(self.__pacientes)

    def excluir_paciente(self):
        cpf = self.__tela.pegar_cpf()

        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                self.__pacientes.remove(paciente)
                self.__tela.mostrar_mensagem("Paciente removido com sucesso.")
                return
        self.__tela.mostrar_mansagem("Paciente não encontrado.")

    def alterar_paciente(self):
        cpf = self.__tela.pegar_cpf()

        for paciente in self.__pacientes:
            if paciente.cpf == cpf:

                nome, celular, = self.__tela.pegar_dados_alteracao()
                paciente.nome = nome
                paciente.celular = celular

                self.__tela.mostrar_mensagem("Paciente alterado com sucesso!")
                return

        print("Paciente não encontrado.")

    def escolher_paciente(self):
        if len(self.__pacientes) == 0:
            print("Nenhum paciente cadastrado.")
            return None

        print("\n=== ESCOLHER PACIENTE ===")

        for i, paciente in enumerate(self.__pacientes):
            print(f"{i + 1} - {paciente.nome}")

        try:
            opcao = int(input("Escolha o paciente: "))

            if opcao < 1 or opcao > len(self.__pacientes):
                print("Opção inválida.")
                return None

            return self.__pacientes[opcao - 1]

        except ValueError:
            print("Digite um número válido.")
            return None

    def abrir_menu(self):
        while True:

            opcao = self.__tela.mostrar_menu()

            if opcao == "1":
                self.cadastrar_paciente()

            elif opcao == "2":
                self.listar_pacientes()

            elif opcao == "3":
                self.excluir_paciente()

            elif opcao == "4":
                self.alterar_paciente()

            elif opcao == "0":
                break
