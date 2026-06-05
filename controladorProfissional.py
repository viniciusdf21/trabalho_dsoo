from profissional import Profissional

class ControladorProfissional:
    def __init__(self):
        self.__profissionais = []

    def cadastrar_profissional(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        celular = input("Celular: ")
        especialidade = input("Especialidade: ")
        registro = input("Registro: ")

        try: 
            profissional = Profissional(nome, cpf, celular, especialidade, registro)
            self.__profissionais.append(profissional)
            print('Profissional cadastrado com sucesso!')

        except ValueError as erro:
            print(erro)

    def listar_profissionais(self):
        for profissional in self.__profissionais:
            print("\n")
            print(profissional.exibir_dados())

    def excluir_profissional(self):
        cpf = input("CPF do profissional: ")

        for profissional in self.__profissionais:
            if profissional.cpf == cpf:
                self.__profissionais.remove(profissional)
                print("Profissional removido com sucesso.")
                return

        print("Profissional não encontrado.")

    def alterar_profissional(self):
        cpf = input("CPF do profissional: ")

        for profissional in self.__profissionais:
            if profissional.cpf == cpf:

                profissional.nome = input("Novo nome: ")
                profissional.celular = input("Novo celular: ")
                profissional.especialidade = input("Nova especialidade: ")
                profissional.registro = input("Novo registro: ")

                print("Profissional alterado com sucesso!")
                return

        print("Profissional não encontrado.")

    def escolher_profissional(self):
        if len(self.__profissionais) == 0:
            print("Nenhum profissional cadastrado.")
            return None

        print("\n=== ESCOLHER PROFISSIONAL ===")

        for i, profissional in enumerate(self.__profissionais):
            print(f"{i + 1} - {profissional.nome}")

        try:
            opcao = int(input("Escolha o profissional: "))

            if opcao < 1 or opcao > len(self.__profissionais):
                print("Opção inválida.")
                return None

            return self.__profissionais[opcao - 1]

        except ValueError:
            print("Digite um número válido.")
            return None

    def abrir_menu(self):
        while True:
            print("\n=== PROFISSIONAIS ===")
            print("1 - Cadastrar")
            print("2 - Listar")
            print("3 - Excluir")
            print("4 - Alterar")
            print("0 - Voltar")

            opcao = input("Opção: ")

            if opcao == "1":
                self.cadastrar_profissional()

            elif opcao == "2":
                self.listar_profissionais()

            elif opcao == "3":
                self.excluir_profissional()

            elif opcao == "4":
                self.alterar_profissional()

            elif opcao == "0":
                break
