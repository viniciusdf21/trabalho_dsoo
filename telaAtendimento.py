from datetime import date, time


class TelaAtendimento:

    def mostrar_menu(self):
        print("\n=== ATENDIMENTOS ===")
        print("1 - Registrar")
        print("2 - Listar")
        print("3 - Alterar")
        print("4 - Excluir")
        print("0 - Voltar")
        return input("Opção: ")


    def mostrar_inicio_alteracao(self):
        print("\n=== ALTERAR ATENDIMENTO ===")
        print("Digite novamente todos os dados do atendimento.")


    def ler_data_atendimento(self):
        return date(
            int(input("Ano do atendimento: ")),
            int(input("Mês do atendimento: ")),
            int(input("Dia do atendimento: "))
        )


    def ler_horario_inicio(self):
        hora_inicio = int(input("Hora de início: "))
        minuto_inicio = int(input("Minuto de início: "))
        return time(hora_inicio, minuto_inicio)


    def ler_horario_fim(self):
        hora_fim = int(input("Hora de fim: "))
        minuto_fim = int(input("Minuto de fim: "))
        return time(hora_fim, minuto_fim)


    def ler_valor(self):
        return float(input("Valor do atendimento: "))


    def mostrar_atendimentos(self, atendimentos):
        if not atendimentos:
            print("Nenhum atendimento cadastrado.")
            return

        for atendimento in atendimentos:
            print("\n")
            print(atendimento.exibir_dados())


    def escolher_atendimento(self, atendimentos):
        if not atendimentos:
            print("Nenhum atendimento cadastrado.")
            return None

        print("\n=== ESCOLHER ATENDIMENTO ===")

        for i, atendimento in enumerate(atendimentos):
            print(f"{i + 1} - {atendimento.paciente.nome} - {atendimento.data}")

        try:
            opcao = int(input("Escolha o atendimento: "))

            if opcao < 1 or opcao > len(atendimentos):
                print("Atendimento inválido.")
                return None

            return atendimentos[opcao - 1]

        except ValueError:
            print("Digite um número válido.")
            return None


    def confirmar_exclusao(self):
        confirmacao = input("Tem certeza que deseja excluir este atendimento? (s/n): ")
        return confirmacao.lower() == "s"


    def mostrar_mensagem(self, mensagem):
        print(mensagem)


    def mostrar_erro_cadastro(self, erro):
        print(f"Erro ao cadastrar atendimento: {erro}")


    def mostrar_erro_alteracao(self, erro):
        print(f"Erro ao alterar atendimento: {erro}")