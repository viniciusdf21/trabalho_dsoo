class TelaPaciente:

    def pegar_dados_paciente(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        celular = input("Celular: ")

        return nome, cpf, celular

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def mostrar_menu(self):
        print("\n=== PACIENTES ===")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Excluir")
        print("4 - Alterar")
        print("0 - Voltar")

        return input("Opção: ")
