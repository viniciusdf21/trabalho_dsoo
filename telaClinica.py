class TelaClinica:

    def pegar_dados_clinica(self):
        nome = input("Nome: ")
        localizacao = input("Localização: ")
        descricao = input("Descrição: ")

        return nome, localizacao, descricao

    def pegar_horarios(self):
        abertura = int(input("Hora abertura: "))
        minuto_abertura = int(input("Minuto abertura: "))

        fechamento = int(input("Hora fechamento: "))
        minuto_fechamento = int(input("Minuto fechamento: "))

        return abertura, minuto_abertura, fechamento, minuto_fechamento

    def mostrar_menu(self):
        print("\n=== CLÍNICA ===")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Excluir")
        print("4 - Alterar")
        print("0 - Voltar")

        return input("Opção: ")
