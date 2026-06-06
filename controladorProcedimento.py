from procedimento import Procedimento


class ControladorProcedimento:
    def registrar_procedimento(self, atendimento, procedimento: Procedimento):
        try:
            atendimento.adicionar_procedimento(procedimento)

            print("Procedimento registrado com sucesso.")
            return procedimento

        except ValueError as erro:
            print(f"Erro ao registrar procedimento: {erro}")
            return None

    def cadastrar_procedimento(self, atendimento):
        try:
            nome = input("Nome do procedimento: ")
            descricao = input("Descrição: ")
            custo = float(input("Custo: "))

            procedimento = Procedimento(nome, descricao, custo, atendimento.profissional)

            self.registrar_procedimento(atendimento, procedimento)

        except ValueError as erro:
            print(f"Erro ao cadastrar procedimento: {erro}")

    def listar_procedimentos(self, atendimento):
        if not atendimento.lista_procedimentos:
            print("Nenhum procedimento registrado.")
            return

        for procedimento in atendimento.lista_procedimentos:
            print("\n")
            print(procedimento.exibir_dados())

    def abrir_menu(self, controlador_atendimento):
        while True:
            print("\n=== PROCEDIMENTOS ===")
            print("1 - Registrar")
            print("2 - Listar")
            print("0 - Voltar")

            opcao = input("Opção: ")

            if opcao == "1":
                atendimento = controlador_atendimento.escolher_atendimento()

                if atendimento is not None:
                    self.cadastrar_procedimento(atendimento)

            elif opcao == "2":
                atendimento = controlador_atendimento.escolher_atendimento()

                if atendimento is not None:
                    self.listar_procedimentos(atendimento)

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")