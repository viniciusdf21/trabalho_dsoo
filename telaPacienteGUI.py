import FreeSimpleGUI as sg


class TelaPaciente:

    def __init__(self):
        self.__window = None

    def mostrar_menu(self):

        layout = [
            [sg.Text("CADASTRO DE PACIENTES")],
            [sg.Button("Cadastrar", size=(20, 2), key="1")],
            [sg.Button("Listar", size=(20, 2), key="2")],
            [sg.Button("Alterar", size=(20, 2), key="3")],
            [sg.Button("Excluir", size=(20, 2), key="4")],
            [sg.Button("Voltar", size=(20, 2), key="0")]
        ]

        self.__window = sg.Window("Menu Pacientes", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento == sg.WINDOW_CLOSED:
            return "0"

        return evento

    def pegar_dados_paciente(self):

        layout = [
            [sg.Text("Nome"), sg.Input(key="nome")],
            [sg.Text("CPF"), sg.Input(key="cpf")],
            [sg.Text("Celular"), sg.Input(key="celular")],

            [sg.Text("Data de nascimento")],
            [sg.Text("Ano"), sg.Input(size=(5, 1), key="ano"),
             sg.Text("Mês"), sg.Input(size=(3, 1), key="mes"),
             sg.Text("Dia"), sg.Input(size=(3, 1), key="dia")],

            [sg.Button("Salvar"), sg.Button("Cancelar")]
        ]

        self.__window = sg.Window("Cadastrar Paciente", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento in (sg.WINDOW_CLOSED, "Cancelar"):
            return None

        return valores

    def mostrar_pacientes(self, pacientes):

        dados = []

        for paciente in pacientes:
            dados.append([
                paciente.nome,
                paciente.cpf,
                paciente.celular,
                paciente.data_nascimento.strftime("%d/%m/%Y"),
                f"{paciente.verificar_idade()} anos"
            ])

        layout = [
            [sg.Text("PACIENTES CADASTRADOS")],

            [sg.Table(
                values=dados,
                headings=["Nome", "CPF", "Celular", "Nascimento", "Idade"],
                auto_size_columns=True,
                justification="center",
                num_rows=8,
                key="tabela",
                select_mode=sg.TABLE_SELECT_MODE_BROWSE
            )],

            [sg.Button("Fechar")]
        ]

        self.__window = sg.Window("Lista de Pacientes", layout)
        self.__window.read()
        self.__window.close()

    def selecionar_paciente(self, pacientes):
        if not pacientes:
            sg.popup("Nenhum paciente cadastrado.")
            return None

        dados = []

        for paciente in pacientes:
            dados.append([
                paciente.nome,
                paciente.cpf,
                paciente.celular
            ])

        layout = [
            [sg.Text("Selecione um paciente")],

            [sg.Table(
                values=dados,
                headings=["Nome", "CPF", "Celular"],
                auto_size_columns=True,
                justification="center",
                num_rows=8,
                key="tabela",
                select_mode=sg.TABLE_SELECT_MODE_BROWSE
            )],

            [sg.Button("Selecionar"), sg.Button("Cancelar")]
        ]

        self.__window = sg.Window("Selecionar Paciente", layout)
        evento, valores = self.__window.read()
        self.__window.close()
        if evento in (sg.WINDOW_CLOSED, "Cancelar"):
            return None

        if not valores["tabela"]:
            return None

        return valores["tabela"][0]

    def alterar_paciente(self, paciente):

        layout = [
            [sg.Text("Nome"), sg.Input(paciente.nome, key="nome")],
            [sg.Text("Celular"), sg.Input(paciente.celular, key="celular")],

            [sg.Button("Salvar"), sg.Button("Cancelar")]
        ]

        self.__window = sg.Window("Alterar Paciente", layout)

        evento, valores = self.__window.read()
        self.__window.close()

        if evento in (sg.WINDOW_CLOSED, "Cancelar"):
            return None

        return valores

    def mostrar_mensagem(self, msg):
        sg.popup(msg)

    def mostrar_erro(self, msg):
        sg.popup_error(msg)

    def confirmar_exclusao(self, nome):
        return sg.popup_yes_no(f"Deseja excluir o paciente {nome}?") == "Yes"
