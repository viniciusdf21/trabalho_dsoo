class TelaTipoAtendimento:

    def pegar_dados_tipo(self):
        nome = input("Nome do tipo de atendimento: ")
        descricao = input("Descrição: ")

        return nome, descricao

    def mostrar_menu(self):
        print("\n=== TIPOS DE ATENDIMENTO ===")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Excluir")
        print("4 - Alterar")
        print("0 - Voltar")

        return input("Opção: ")
