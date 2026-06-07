from datetime import date


class TelaPagamento:

    def mostrar_menu(self):
        print("\n=== PAGAMENTOS ===")
        print("1 - Registrar")
        print("2 - Listar")
        print("3 - Alterar")
        print("4 - Excluir")
        print("0 - Voltar")
        return input("Opção: ")

    def mostrar_menu_tipo_pagamento(self):
        print("\n=== TIPO DE PAGAMENTO ===")
        print("1 - Dinheiro")
        print("2 - Pix")
        print("3 - Cartão de crédito")
        return input("Opção: ")

    def ler_data_pagamento(self):
        return date(
            int(input("Ano do pagamento: ")),
            int(input("Mês do pagamento: ")),
            int(input("Dia do pagamento: "))
        )

    def ler_valor_pago(self):
        return float(input("Valor pago: "))

    def ler_cpf_pagante(self):
        return input("CPF do pagante: ")

    def ler_numero_cartao(self):
        return input("Número do cartão: ")

    def ler_bandeira(self):
        return input("Bandeira: ")

    def mostrar_inicio_alteracao(self):
        print("\n=== ALTERAR PAGAMENTO ===")
        print("Digite novamente os dados do pagamento.")

    def mostrar_pagamentos(self, atendimento):
        if not atendimento.lista_pagamentos:
            print("Nenhum pagamento registrado.")
            return

        for pagamento in atendimento.lista_pagamentos:
            print("\n")
            print(f"Tipo: {pagamento.__class__.__name__}")
            print(f"Data: {pagamento.data}")
            print(f"Valor pago: R$ {pagamento.valor_pago:.2f}")

        print(f"\nValor restante: R$ {atendimento.calcular_valor_restante():.2f}")

    def escolher_pagamento(self, atendimento):
        if not atendimento.lista_pagamentos:
            print("Nenhum pagamento registrado.")
            return None

        print("\n=== ESCOLHER PAGAMENTO ===")

        for i, pagamento in enumerate(atendimento.lista_pagamentos):
            print(
                f"{i + 1} - {pagamento.__class__.__name__} "
                f"- R$ {pagamento.valor_pago:.2f} - {pagamento.data}"
            )

        try:
            opcao = int(input("Escolha o pagamento: "))

            if opcao < 1 or opcao > len(atendimento.lista_pagamentos):
                print("Pagamento inválido.")
                return None

            return atendimento.lista_pagamentos[opcao - 1]

        except ValueError:
            print("Digite um número válido.")
            return None

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def mostrar_erro_registro(self, erro):
        print(f"Erro ao registrar pagamento: {erro}")

    def mostrar_erro_cadastro(self, erro):
        print(f"Erro ao cadastrar pagamento: {erro}")

    def mostrar_erro_alteracao(self, erro):
        print(f"Erro ao alterar pagamento: {erro}")