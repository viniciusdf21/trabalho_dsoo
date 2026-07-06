import FreeSimpleGUI as sg


class TelaTipoAtendimento:

    def __init__(self):
        self.__window = None

    def mostrar_menu(self):

        layout = [
            [sg.Text("TIPOS DE ATENDIMENTO")],
            [sg.Button("Cadastrar", size=(20, 2), key="1")],
            [sg.Button("Listar", size=(20, 2), key="2")],
            [sg.Button("Excluir", size=(20, 2), key="3")],
            [sg.Button("Alterar", size=(20, 2), key="4")],
            [sg.Button("Voltar", size=(20, 2), key="0")]
        ]

        self.__window = sg.Window("Menu Tipos de Atendimento", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento == sg.WINDOW_CLOSED:
            return "0"

        return evento


    def pegar_dados_tipo(self):

        layout = [

            [sg.Text("Nome"),
             sg.Input(key="nome")],
            [sg.Text("Descrição"),
             sg.Input(key="descricao")],
            [sg.Text("Valor Base"),
             sg.Input(key="valor")],
            [sg.Button("Salvar"),
             sg.Button("Cancelar")]
        ]

        self.__window = sg.Window("Cadastrar Tipo de Atendimento", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento in (sg.WINDOW_CLOSED, "Cancelar"):
            return None

        return valores

    def mostrar_tipos_atendimento(self, tipos):
        dados = []

        for tipo in tipos:
            dados.append([
                tipo.nome,
                tipo.descricao,
                f"R$ {tipo.valor_base:.2f}"
            ])

        layout = [
            [sg.Text("Tipos de Atendimento")],
            [sg.Table(
                values=dados,
                headings=["Nome", "Descrição", "Valor Base"],
                auto_size_columns=True,
                justification="center",
                num_rows=8,
                key="tabela",
                select_mode=sg.TABLE_SELECT_MODE_BROWSE
            )],

            [sg.Button("Fechar")]

        ]

        self.__window = sg.Window("Lista de Tipos", layout)
        self.__window.read()
        self.__window.close()

    def selecionar_tipo(self, tipos):

        if not tipos:
            self.mostrar_erro("Nenhum tipo de atendimento cadastrado.")
            return None

        dados = []
        for tipo in tipos:
            dados.append([
                tipo.nome,
                f"R$ {tipo.valor_base:.2f}"
            ])

        layout = [
            [sg.Text("Selecione um tipo de atendimento")],
            [sg.Table(
                values=dados,
                headings=["Nome", "Valor Base"],
                auto_size_columns=True,
                justification="center",
                num_rows=8,
                key="tabela",
                select_mode=sg.TABLE_SELECT_MODE_BROWSE
            )],

            [sg.Button("Selecionar"),
             sg.Button("Cancelar")]

        ]

        self.__window = sg.Window("Selecionar Tipo", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento in (sg.WINDOW_CLOSED, "Cancelar"):
            return None

        if not valores["tabela"]:
            return None

        return valores["tabela"][0]

    def alterar_tipo(self, tipo):

        layout = [
            [sg.Text("Nome"),
             sg.Input(tipo.nome, key="nome")],
            [sg.Text("Descrição"),
             sg.Input(tipo.descricao, key="descricao")],
            [sg.Text("Valor Base"),
             sg.Input(tipo.valor_base, key="valor")],
            [sg.Button("Salvar"),
             sg.Button("Cancelar")]
        ]

        self.__window = sg.Window("Alterar Tipo de Atendimento", layout)
        evento, valores = self.__window.read()
        self.__window.close()
        if evento in (sg.WINDOW_CLOSED, "Cancelar"):
            return None

        return valores

    def confirmar_exclusao(self, nome):

        resposta = sg.popup_yes_no(f"Deseja excluir o tipo de atendimento '{nome}'?")

        return resposta == "Yes"

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem)

    def mostrar_erro(self, mensagem):
        sg.popup_error(mensagem)
