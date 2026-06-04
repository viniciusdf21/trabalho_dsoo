from profissional import Profissional

class ControladorProfissional(Profissional):
    def __init__(self):
        self.__profissionais = []

    def cadastrar_profissional(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Celular: ")
        especialidade = input("Especialidade: ")
        registro = input("Registro: ")

        profissional = Profissional(nome, cpf, celular, especialidade, registro)
        self.__profissionais.append(profissional)

    def listar_profissionais(self):
        for profissional in self.__profissionais:
            print("\n")
            print(profissional.exibir_dados())

    def abrir_menu(self):
        while True:
            print("\n=== PROFISSIONAIS ===")
            print("1 - Cadastrar")
            print("2 - Listar")
            print("0 - Voltar")

            opcao = input("Opção: ")

            if opcao == "1":
                self.cadastrar_profissional()

            elif opcao == "2":
                self.listar_profissionais()

            elif opcao == "0":
                break
