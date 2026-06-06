from datetime import date

from pagamento import Pagamento
from dinheiro import Dinheiro
from pix import Pix
from cartão import CartaoCredito


class ControladorPagamento:
    def registrar_pagamento(self, pagamento: Pagamento):
        try:
            pagamento.registrar_pagamento()
            pagamento.atendimento.adicionar_pagamento(pagamento)

            print("Pagamento registrado com sucesso.")

        except ValueError as erro:
            print(f"Erro ao registrar pagamento: {erro}")

    def cadastrar_pagamento(self, atendimento):
        try:
            data_pagamento = date(
                int(input("Ano do pagamento: ")),
                int(input("Mês do pagamento: ")),
                int(input("Dia do pagamento: "))
            )

            valor_pago = float(input("Valor pago: "))

            print("\n1 - Dinheiro")
            print("2 - Pix")
            print("3 - Cartão de crédito")
            opcao = input("Opção: ")

            if opcao == "1":
                pagamento = Dinheiro(data_pagamento, atendimento, atendimento.paciente, valor_pago)

            elif opcao == "2":
                cpf_pagante = input("CPF do pagante: ")
                pagamento = Pix(data_pagamento, atendimento, atendimento.paciente, valor_pago, cpf_pagante)

            elif opcao == "3":
                numero = input("Número do cartão: ")
                bandeira = input("Bandeira: ")
                pagamento = CartaoCredito(data_pagamento, atendimento, atendimento.paciente, valor_pago, numero, bandeira)

            else:
                print("Opção inválida.")
                return

            self.registrar_pagamento(pagamento)

        except ValueError as erro:
            print(f"Erro ao cadastrar pagamento: {erro}")

    def listar_pagamentos(self, atendimento):
        if not atendimento.lista_pagamentos:
            print("Nenhum pagamento registrado.")
            return

        for pagamento in atendimento.lista_pagamentos:
            print("\n")
            print(f"Tipo: {pagamento.__class__.__name__}")
            print(f"Data: {pagamento.data}")
            print(f"Valor pago: R$ {pagamento.valor_pago:.2f}")

        print(f"\nValor restante: R$ {atendimento.calcular_valor_restante():.2f}")

    def abrir_menu(self, controlador_atendimento):
        while True:
            print("\n=== PAGAMENTOS ===")
            print("1 - Registrar")
            print("2 - Listar")
            print("0 - Voltar")

            opcao = input("Opção: ")

            if opcao == "1":
                atendimento = controlador_atendimento.escolher_atendimento()

                if atendimento is not None:
                    self.cadastrar_pagamento(atendimento)

            elif opcao == "2":
                atendimento = controlador_atendimento.escolher_atendimento()

                if atendimento is not None:
                    self.listar_pagamentos(atendimento)

            elif opcao == "0":
                break

