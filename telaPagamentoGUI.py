from datetime import date
import FreeSimpleGUI as sg


class TelaPagamento:
    def __init__(self):
        self.__window = None

    def mostrar_menu(self):
        layout = [
            [sg.Text("PAGAMENTOS")],
            [sg.Button("Registrar", key="1")],
            [sg.Button("Listar", key="2")],
            [sg.Button("Alterar", key="3")],
            [sg.Button("Excluir", key="4")],
            [sg.Button("Voltar", key="0")]
        ]

        self.__window = sg.Window("Menu Pagamentos", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento == sg.WINDOW_CLOSED:
            return "0"

        return evento

    def mostrar_menu_tipo_pagamento(self):
        layout = [
            [sg.Text("TIPO DE PAGAMENTO")],
            [sg.Button("Dinheiro", key="1")],
            [sg.Button("Pix", key="2")],
            [sg.Button("Cartão de crédito", key="3")],
            [sg.Button("Cancelar", key="0")]
        ]

        self.__window = sg.Window("Tipo de Pagamento", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento == sg.WINDOW_CLOSED:
            return "0"

        return evento

    def ler_data_pagamento(self):
        dia = sg.popup_get_text("Dia do pagamento:")
        mes = sg.popup_get_text("Mês do pagamento:")
        ano = sg.popup_get_text("Ano do pagamento:")

        if dia is None or mes is None or ano is None:
            raise ValueError("Operação cancelada.")

        try:
            return date(int(ano), int(mes), int(dia))

        except ValueError:
            raise ValueError("Data inválida.")

    def ler_valor_pago(self):
        valor = sg.popup_get_text("Valor pago:")

        if valor is None:
            raise ValueError("Operação cancelada.")

        try:
            valor = float(valor.replace(",", "."))

            if valor <= 0:
                raise ValueError("O valor pago deve ser maior que zero.")

            return valor

        except ValueError:
            raise ValueError("Valor inválido.")

    def ler_cpf_pagante(self):
        cpf = sg.popup_get_text("CPF do pagante:")

        if cpf is None:
            raise ValueError("Operação cancelada.")

        cpf = cpf.strip()

        if cpf == "":
            raise ValueError("O CPF do pagante não pode ser vazio.")

        return cpf

    def ler_numero_cartao(self):
        numero = sg.popup_get_text("Número do cartão:")

        if numero is None:
            raise ValueError("Operação cancelada.")

        numero = numero.strip()

        if numero == "":
            raise ValueError("O número do cartão não pode ser vazio.")

        return numero

    def ler_bandeira(self):
        bandeira = sg.popup_get_text("Bandeira do cartão:")

        if bandeira is None:
            raise ValueError("Operação cancelada.")

        bandeira = bandeira.strip()

        if bandeira == "":
            raise ValueError("A bandeira do cartão não pode ser vazia.")

        return bandeira

    def mostrar_inicio_alteracao(self):
        sg.popup("Digite novamente os dados do pagamento.")

    def mostrar_pagamentos(self, atendimento):
        if not atendimento.lista_pagamentos:
            sg.popup("Nenhum pagamento registrado.")
            return

        texto = ""

        for pagamento in atendimento.lista_pagamentos:
            texto += f"Tipo: {pagamento.__class__.__name__}\n"
            texto += f"Data: {pagamento.data}\n"
            texto += f"Valor pago: R$ {pagamento.valor_pago:.2f}\n"
            texto += "\n-----------------------------\n\n"

        texto += f"Valor restante: R$ {atendimento.calcular_valor_restante():.2f}"

        sg.popup_scrolled(
            texto,
            title="Pagamentos registrados",
            size=(70, 20)
        )

    def escolher_pagamento(self, atendimento):
        if not atendimento.lista_pagamentos:
            sg.popup("Nenhum pagamento registrado.")
            return None

        opcoes = []

        for i, pagamento in enumerate(atendimento.lista_pagamentos):
            texto = (
                f"{i + 1} - "
                f"{pagamento.__class__.__name__} - "
                f"R$ {pagamento.valor_pago:.2f} - "
                f"{pagamento.data}"
            )
            opcoes.append(texto)

        layout = [
            [sg.Text("Escolha um pagamento:")],
            [sg.Listbox(opcoes, size=(50, 8), key="pagamento")],
            [sg.Button("Selecionar"), sg.Button("Cancelar")]
        ]

        self.__window = sg.Window("Escolher Pagamento", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento in (sg.WINDOW_CLOSED, "Cancelar"):
            return None

        if not valores["pagamento"]:
            sg.popup("Selecione um pagamento.")
            return None

        escolhido = valores["pagamento"][0]
        indice = opcoes.index(escolhido)

        return atendimento.lista_pagamentos[indice]

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem)

    def mostrar_erro_registro(self, erro):
        sg.popup(f"Erro ao registrar pagamento: {erro}")

    def mostrar_erro_cadastro(self, erro):
        sg.popup(f"Erro ao cadastrar pagamento: {erro}")

    def mostrar_erro_alteracao(self, erro):
        sg.popup(f"Erro ao alterar pagamento: {erro}")
