class TelaProfissional:

    def pegar_dados_profissional(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        celular = input("Celular: ")
        especialidade = input("Especialidade: ")
        registro = input("Registro: ")

        return (nome,cpf,celular,especialidade,registro)

    def mostrar_menu(self):
        print("\n=== PROFISSIONAIS ===")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Excluir")
        print("4 - Alterar")
        print("0 - Voltar")

        return input("Opção: ")
