import FreeSimpleGUI as sg


class TelaProfissional:

    def __init__(self):
        self.__window = None

    def mostrar_menu(self):

        layout = [
            [sg.Text("CADASTRO DE PROFISSIONAIS")],
            [sg.Button("Cadastrar", size=(20, 2), key="1")],
            [sg.Button("Listar", size=(20, 2), key="2")],
            [sg.Button("Excluir", size=(20, 2), key="3")],
            [sg.Button("Alterar", size=(20, 2), key="4")],
            [sg.Button("Voltar", size=(20, 2), key="0")]
        ]

        self.__window = sg.Window("Menu Profissionais", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento == sg.WINDOW_CLOSED:
            return "0"

        return evento

    def pegar_dados_profissional(self):

        layout = [

            [sg.Text("Nome"),
             sg.Input(key="nome")],
            [sg.Text("CPF"),
             sg.Input(key="cpf")],
            [sg.Text("Celular"),
             sg.Input(key="celular")],
            [sg.Text("Especialidade"),
             sg.Input(key="especialidade")],
            [sg.Text("Registro"),
             sg.Input(key="registro")],
            [sg.Button("Salvar"),
             sg.Button("Cancelar")]

        ]

        self.__window = sg.Window("Cadastrar Profissional", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento in (sg.WINDOW_CLOSED, "Cancelar"):
            return None

        return valores

    def mostrar_profissionais(self, profissionais):
        dados = []

        for profissional in profissionais:
            dados.append([
                profissional.nome,
                profissional.cpf,
                profissional.celular,
                profissional.especialidade,
                profissional.registro
            ])

        layout = [
            [sg.Text("Profissionais cadastrados")],
            [sg.Table(
                values=dados,
                headings=["Nome", "CPF", "Celular", "Especialidade", "Registro"],
                auto_size_columns=True,
                justification="center",
                num_rows=8,
                key="tabela",
                select_mode=sg.TABLE_SELECT_MODE_BROWSE
            )],

            [sg.Button("Fechar")]

        ]

        self.__window = sg.Window("Lista de Profissionais", layout)
        self.__window.read()
        self.__window.close()

    def selecionar_profissional(self, profissionais):

        if not profissionais:
            self.mostrar_erro("Nenhum profissional cadastrado.")
            return None

        dados = []
        for profissional in profissionais:
            dados.append([
                profissional.nome,
                profissional.cpf,
                profissional.especialidade
            ])

        layout = [
            [sg.Text("Selecione um profissional")],

            [sg.Table(
                values=dados,
                headings=["Nome", "CPF", "Especialidade"],
                auto_size_columns=True,
                justification="center",
                num_rows=8,
                key="tabela",
                select_mode=sg.TABLE_SELECT_MODE_BROWSE
            )],

            [sg.Button("Selecionar"), sg.Button("Cancelar")]
        ]

        self.__window = sg.Window("Selecionar Profissional", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento in (sg.WINDOW_CLOSED, "Cancelar"):
            return None

        if not valores["tabela"]:
            return None

        return valores["tabela"][0]


    def alterar_profissional(self, profissional):

        layout = [

            [sg.Text("Nome"),
             sg.Input(profissional.nome, key="nome")],
            [sg.Text("Celular"),
             sg.Input(profissional.celular, key="celular")],
            [sg.Text("Especialidade"),
             sg.Input(profissional.especialidade, key="especialidade")],
            [sg.Text("Registro"),
             sg.Input(profissional.registro, key="registro")],
            [sg.Button("Salvar"),
             sg.Button("Cancelar")]
        ]

        self.__window = sg.Window("Alterar Profissional", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento in (sg.WINDOW_CLOSED, "Cancelar"):
            return None

        return valores


    def confirmar_exclusao(self, nome):
        resposta = sg.popup_yes_no(f"Deseja excluir o profissional {nome}?")
        return resposta == "Yes"

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem)

    def mostrar_erro(self, mensagem):
        sg.popup_error(mensagem)
