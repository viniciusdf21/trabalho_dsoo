from pagamento import Pagamento
from dinheiro import Dinheiro
from pix import Pix
from cartão import CartaoCredito
from telaPagamento import TelaPagamento


class ControladorPagamento:
    def __init__(self):
        self.__tela_pagamento = TelaPagamento()


    def registrar_pagamento(self, pagamento: Pagamento):
        try:
            pagamento.registrar_pagamento()
            pagamento.atendimento.adicionar_pagamento(pagamento)

            self.__tela_pagamento.mostrar_mensagem("Pagamento registrado com sucesso.")

        except ValueError as erro:
            self.__tela_pagamento.mostrar_erro_registro(erro)


    def cadastrar_pagamento(self, atendimento):
        try:
            data_pagamento = self.__tela_pagamento.ler_data_pagamento()
            valor_pago = self.__tela_pagamento.ler_valor_pago()

            opcao = self.__tela_pagamento.mostrar_menu_tipo_pagamento()

            if opcao == "1":
                pagamento = Dinheiro(
                    data_pagamento,atendimento, atendimento.paciente, valor_pago)

            elif opcao == "2":
                cpf_pagante = self.__tela_pagamento.ler_cpf_pagante()

                pagamento = Pix(
                    data_pagamento, atendimento,atendimento.paciente, valor_pago, cpf_pagante)

            elif opcao == "3":
                numero = self.__tela_pagamento.ler_numero_cartao()
                bandeira = self.__tela_pagamento.ler_bandeira()

                pagamento = CartaoCredito(data_pagamento, atendimento, atendimento.paciente, valor_pago, numero, bandeira)

            else:
                self.__tela_pagamento.mostrar_mensagem("Opção inválida.")
                return

            self.registrar_pagamento(pagamento)

        except ValueError as erro:
            self.__tela_pagamento.mostrar_erro_cadastro(erro)


    def listar_pagamentos(self, atendimento):
        self.__tela_pagamento.mostrar_pagamentos(atendimento)


    def escolher_pagamento(self, atendimento):
        return self.__tela_pagamento.escolher_pagamento(atendimento)


    def alterar_pagamento(self, atendimento):
        pagamento = self.escolher_pagamento(atendimento)

        if pagamento is None:
            return

        try:
            self.__tela_pagamento.mostrar_inicio_alteracao()

            nova_data = self.__tela_pagamento.ler_data_pagamento()
            novo_valor_pago = self.__tela_pagamento.ler_valor_pago()

            pagamento.data = nova_data
            pagamento.valor_pago = novo_valor_pago

            if isinstance(pagamento, Pix):
                novo_cpf_pagante = self.__tela_pagamento.ler_cpf_pagante()
                pagamento.cpf_pagante = novo_cpf_pagante

            elif isinstance(pagamento, CartaoCredito):
                novo_numero = self.__tela_pagamento.ler_numero_cartao()
                nova_bandeira = self.__tela_pagamento.ler_bandeira()

                pagamento.numero = novo_numero
                pagamento.bandeira = nova_bandeira

            pagamento.registrar_pagamento()

            self.__tela_pagamento.mostrar_mensagem("Pagamento alterado com sucesso.")

        except ValueError as erro:
            self.__tela_pagamento.mostrar_erro_alteracao(erro)


    def excluir_pagamento(self, atendimento):
        pagamento = self.escolher_pagamento(atendimento)

        if pagamento is None:
            return

        atendimento.lista_pagamentos.remove(pagamento)

        self.__tela_pagamento.mostrar_mensagem("Pagamento excluído com sucesso.")


    def abrir_menu(self, controlador_atendimento):
        while True:
            opcao = self.__tela_pagamento.mostrar_menu()

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
                self.__tela_pagamento.mostrar_mensagem("Opção inválida.")

