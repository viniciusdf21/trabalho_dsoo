class TelaPrincipal:

    def mostrar_menu(self):
        print("\n=== SISTEMA DA CLÍNICA ===")
        print("1 - Pacientes")
        print("2 - Profissionais")
        print("3 - Clínica")
        print("4 - Tipos de atendimentos")
        print("5 - Atendimentos")
        print("6 - Pagamentos")
        print("7 - Procedimentos")
        print("8 - Relatórios")
        print("0 - Sair")

        return input("Escolha uma opção: ")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
