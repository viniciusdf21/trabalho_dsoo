from datetime import date, time
import FreeSimpleGUI as sg


class TelaAtendimento:
    def __init__(self):
        self.__window = None

    def mostrar_menu(self):
        layout = [
            [sg.Text("ATENDIMENTOS")],
            [sg.Button("Cadastrar", key="1")],
            [sg.Button("Listar", key="2")],
            [sg.Button("Alterar", key="3")],
            [sg.Button("Excluir", key="4")],
            [sg.Button("Voltar", key="0")]
        ]

        self.__window = sg.Window("Menu Atendimentos", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento == sg.WINDOW_CLOSED:
            return "0"

        return evento

    def ler_data_atendimento(self):
        dia = sg.popup_get_text("Digite o dia:")
        mes = sg.popup_get_text("Digite o mês:")
        ano = sg.popup_get_text("Digite o ano:")

        if dia is None or mes is None or ano is None:
            raise ValueError("Operação cancelada.")

        try:
            return date(int(ano), int(mes), int(dia))
        except ValueError:
            raise ValueError("Data inválida.")

    def ler_horario_inicio(self):
        return self.__ler_horario("início")

    def ler_horario_fim(self):
        return self.__ler_horario("fim")

    def __ler_horario(self, tipo):
        hora = sg.popup_get_text(f"Digite a hora de {tipo}:")
        minuto = sg.popup_get_text(f"Digite o minuto de {tipo}:")

        if hora is None or minuto is None:
            raise ValueError("Operação cancelada.")

        try:
            return time(int(hora), int(minuto))
        except ValueError:
            raise ValueError("Horário inválido.")

    def ler_valor(self):
        valor = sg.popup_get_text("Digite o valor do atendimento:")

        if valor is None:
            raise ValueError("Operação cancelada.")

        try:
            valor = float(valor.replace(",", "."))

            if valor <= 0:
                raise ValueError("O valor deve ser maior que zero.")

            return valor

        except ValueError:
            raise ValueError("Valor inválido.")

    def mostrar_atendimentos(self, atendimentos):
        if not atendimentos:
            sg.popup("Nenhum atendimento cadastrado.")
            return

        texto = ""

        for atendimento in atendimentos:
            texto += atendimento.exibir_dados()
            texto += "\n\n-----------------------------\n\n"

        sg.popup_scrolled(texto, title="Atendimentos cadastrados", size=(70, 20))

    def escolher_atendimento(self, atendimentos):
        if not atendimentos:
            sg.popup("Nenhum atendimento cadastrado.")
            return None

        opcoes = []

        for i, atendimento in enumerate(atendimentos):
            texto = f"{i + 1} - {atendimento.paciente.nome} - {atendimento.data}"
            opcoes.append(texto)

        layout = [
            [sg.Text("Escolha um atendimento:")],
            [sg.Listbox(opcoes, size=(50, 8), key="atendimento")],
            [sg.Button("Selecionar"), sg.Button("Cancelar")]
        ]

        self.__window = sg.Window("Escolher Atendimento", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento in (sg.WINDOW_CLOSED, "Cancelar"):
            return None

        if not valores["atendimento"]:
            sg.popup("Selecione um atendimento.")
            return None

        escolhido = valores["atendimento"][0]
        indice = opcoes.index(escolhido)

        return atendimentos[indice]

    def confirmar_exclusao(self):
        resposta = sg.popup_yes_no(
            "Tem certeza que deseja excluir este atendimento?",
            custom_text=("Sim", "Não")
        )

        return resposta == "Sim"

    def mostrar_inicio_alteracao(self):
        sg.popup("Digite novamente os dados do atendimento.")

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem)

    def mostrar_erro_cadastro(self, erro):
        sg.popup(f"Erro ao cadastrar atendimento: {erro}")

    def mostrar_erro_alteracao(self, erro):
        sg.popup(f"Erro ao alterar atendimento: {erro}")
