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

    def escolher_pagamento(self, atendimento):
        if not atendimento.lista_pagamentos:
            print("Nenhum pagamento registrado.")
            return None

        print("\n=== ESCOLHER PAGAMENTO ===")

        for i, pagamento in enumerate(atendimento.lista_pagamentos):
            print(f"{i + 1} - {pagamento.__class__.__name__} - R$ {pagamento.valor_pago:.2f} - {pagamento.data}")

        try:
            opcao = int(input("Escolha o pagamento: "))

            if opcao < 1 or opcao > len(atendimento.lista_pagamentos):
                print("Pagamento inválido.")
                return None

            return atendimento.lista_pagamentos[opcao - 1]

        except ValueError:
            print("Digite um número válido.")
            return None

    def alterar_pagamento(self, atendimento):
        pagamento = self.escolher_pagamento(atendimento)

        if pagamento is None:
            return

        while True:
            print("\n=== ALTERAR PAGAMENTO ===")
            print("1 - Alterar data")
            print("2 - Alterar valor pago")

            if isinstance(pagamento, Pix):
                print("3 - Alterar CPF do pagante")

            elif isinstance(pagamento, CartaoCredito):
                print("3 - Alterar número do cartão")
                print("4 - Alterar bandeira")

            print("0 - Voltar")

            opcao = input("Opção: ")

            try:
                if opcao == "1":
                    nova_data = date(
                        int(input("Novo ano do pagamento: ")),
                        int(input("Novo mês do pagamento: ")),
                        int(input("Novo dia do pagamento: "))
                    )

                    pagamento.data = nova_data
                    pagamento.registrar_pagamento()
                    print("Data do pagamento alterada com sucesso.")

                elif opcao == "2":
                    pagamento.valor_pago = float(input("Novo valor pago: "))
                    pagamento.registrar_pagamento()
                    print("Valor pago alterado com sucesso.")

                elif opcao == "3" and isinstance(pagamento, Pix):
                    pagamento.cpf_pagante = input("Novo CPF do pagante: ")
                    print("CPF do pagante alterado com sucesso.")

                elif opcao == "3" and isinstance(pagamento, CartaoCredito):
                    pagamento.numero = input("Novo número do cartão: ")
                    print("Número do cartão alterado com sucesso.")

                elif opcao == "4" and isinstance(pagamento, CartaoCredito):
                    pagamento.bandeira = input("Nova bandeira: ")
                    print("Bandeira alterada com sucesso.")

                elif opcao == "0":
                    break

                else:
                    print("Opção inválida.")

            except ValueError as erro:
                print(f"Erro ao alterar pagamento: {erro}")

    def excluir_pagamento(self, atendimento):
        pagamento = self.escolher_pagamento(atendimento)

        if pagamento is None:
            return

        confirmacao = input("Tem certeza que deseja excluir este pagamento? (s/n): ")

        if confirmacao.lower() == "s":
            atendimento.lista_pagamentos.remove(pagamento)
            print("Pagamento excluído com sucesso.")
        else:
            print("Exclusão cancelada.")

    def abrir_menu(self, controlador_atendimento):
        while True:
            print("\n=== PAGAMENTOS ===")
            print("1 - Registrar")
            print("2 - Listar")
            print("3 - Alterar")
            print("4 - Excluir")
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

            elif opcao == "3":
                atendimento = controlador_atendimento.escolher_atendimento()

                if atendimento is not None:
                    self.alterar_pagamento(atendimento)

            elif opcao == "4":
                atendimento = controlador_atendimento.escolher_atendimento()

                if atendimento is not None:
                    self.excluir_pagamento(atendimento)

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")

