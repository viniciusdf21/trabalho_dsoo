class TelaProcedimento:

    def mostrar_menu(self):
        print("\n=== PROCEDIMENTOS ===")
        print("1 - Registrar")
        print("2 - Listar")
        print("3 - Alterar")
        print("4 - Excluir")
        print("0 - Voltar")
        return input("Opção: ")

    def ler_nome(self):
        return input("Nome do procedimento: ")

    def ler_descricao(self):
        return input("Descrição: ")

    def ler_custo(self):
        return float(input("Custo: "))

    def mostrar_inicio_alteracao(self):
        print("\n=== ALTERAR PROCEDIMENTO ===")
        print("Digite novamente os dados do procedimento.")

    def mostrar_procedimentos(self, atendimento):
        if not atendimento.lista_procedimentos:
            print("Nenhum procedimento registrado.")
            return

        for procedimento in atendimento.lista_procedimentos:
            print("\n")
            print(procedimento.exibir_dados())

    def escolher_procedimento(self, atendimento):
        if not atendimento.lista_procedimentos:
            print("Nenhum procedimento registrado.")
            return None

        print("\n=== ESCOLHER PROCEDIMENTO ===")

        for i, procedimento in enumerate(atendimento.lista_procedimentos):
            print(f"{i + 1} - {procedimento.nome} - R$ {procedimento.custo:.2f}")

        try:
            opcao = int(input("Escolha o procedimento: "))

            if opcao < 1 or opcao > len(atendimento.lista_procedimentos):
                print("Procedimento inválido.")
                return None

            return atendimento.lista_procedimentos[opcao - 1]

        except ValueError:
            print("Digite um número válido.")
            return None

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def mostrar_erro_registro(self, erro):
        print(f"Erro ao registrar procedimento: {erro}")

    def mostrar_erro_cadastro(self, erro):
        print(f"Erro ao cadastrar procedimento: {erro}")

    def mostrar_erro_alteracao(self, erro):
        print(f"Erro ao alterar procedimento: {erro}")