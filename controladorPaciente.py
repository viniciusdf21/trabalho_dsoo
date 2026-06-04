from paciente import Paciente
from datetime import date


class ControladorPaciente(Paciente):
    def __init__(self):
        self.__pacientes = []

    def cadastrar_paciente(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        celular = input("Celular: ")

        ano = int(input("Ano de nascimento: "))
        mes = int(input("Mês de nascimento: "))
        dia = int(input("Dia de nascimento: "))

        data_nascimento = date(ano, mes, dia)

        paciente = Paciente(nome, cpf, celular, data_nascimento)
        self.__pacientes.append(paciente)

    def listar_pacientes(self):
        for paciente in self.__pacientes:
            print("\n")
            print(paciente.exibir_dados())

    def abrir_menu(self):
        while True:
            print("\n=== PACIENTES ===")
            print("1 - Cadastrar")
            print("2 - Listar")
            print("0 - Voltar")

            opcao = input("Opção: ")

            if opcao == "1":
                self.cadastrar_paciente()

            elif opcao == "2":
                self.listar_pacientes()

            elif opcao == "0":
                break
