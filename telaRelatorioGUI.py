import FreeSimpleGUI as sg


class TelaRelatorio:
    def __init__(self):
        self.__window = None


    def mostrar_menu(self):
        layout = [
            [sg.Text("RELATÓRIOS")],
            [sg.Button("Atendimento mais caro e mais barato", key="1")],
            [sg.Button("Voltar", key="0")]
        ]

        self.__window = sg.Window("Menu Relatórios", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento == sg.WINDOW_CLOSED:
            return "0"

        return evento


    def mostrar_relatorio_atendimento_mais_caro_barato(self, atendimento_mais_caro, atendimento_mais_barato):
        texto = "=== ATENDIMENTO MAIS CARO ===\n\n"
        texto += atendimento_mais_caro.exibir_dados()s

        texto += "\n\n-----------------------------\n\n"

        texto += "=== ATENDIMENTO MAIS BARATO ===\n\n"
        texto += atendimento_mais_barato.exibir_dados()

        sg.popup_scrolled(
            texto,
            title="Atendimento mais caro e mais barato",
            size=(70, 20)
        )


    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem)
