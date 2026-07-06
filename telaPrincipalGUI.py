import FreeSimpleGUI as sg


class TelaPrincipal:
    def __init__(self):
        self.__window = None

    def mostrar_menu(self):
        layout = [
            [sg.Text("SISTEMA DA CLÍNICA", font=("Arial", 16))],
            [sg.Button("Pacientes", key="1", size=(25, 1))],
            [sg.Button("Profissionais", key="2", size=(25, 1))],
            [sg.Button("Clínicas", key="3", size=(25, 1))],
            [sg.Button("Tipos de Atendimento", key="4", size=(25, 1))],
            [sg.Button("Atendimentos", key="5", size=(25, 1))],
            [sg.Button("Pagamentos", key="6", size=(25, 1))],
            [sg.Button("Procedimentos", key="7", size=(25, 1))],
            [sg.Button("Relatórios", key="8", size=(25, 1))],
            [sg.HorizontalSeparator()],
            [sg.Button("Sair", key="0", size=(25, 1))]
        ]

        self.__window = sg.Window("Sistema Clínica", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento == sg.WINDOW_CLOSED:
            return "0"
        return evento

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem)

    def mostrar_erro(self, mensagem):
        sg.popup_error(mensagem)
