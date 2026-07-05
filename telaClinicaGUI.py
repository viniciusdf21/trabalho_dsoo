import FreeSimpleGUI as sg


class TelaClinica:

    def __init__(self):
        sg.theme("LightBlue3")

    def mostrar_menu(self):

        layout = [
            [sg.Text("GERENCIAMENTO DE CLÍNICAS",
                     font=("Arial", 16, "bold"),
                     justification="center",
                     expand_x=True)],

            [sg.Button("Cadastrar", size=(20, 2), key="1")],
            [sg.Button("Listar", size=(20, 2), key="2")],
            [sg.Button("Alterar", size=(20, 2), key="3")],
            [sg.Button("Excluir", size=(20, 2), key="4")],

            [sg.Push(), sg.Button("Voltar", key="0"), sg.Push()]
        ]

        window = sg.Window("Clínicas", layout)

        evento, _ = window.read()
        window.close()

        if evento == sg.WIN_CLOSED:
            return "0"

        return evento

    def pegar_dados_clinica(self):

        layout = [

            [sg.Text("Nome", size=(15,1)),
             sg.Input(key="nome")],

            [sg.Text("Localização", size=(15,1)),
             sg.Input(key="loc")],

            [sg.Text("Descrição", size=(15,1)),
             sg.Input(key="descricao")],

            [sg.Text("Hora abertura"),
             sg.Input(size=(4,1), key="ha"),
             sg.Text(":"),
             sg.Input(size=(4,1), key="ma")],

            [sg.Text("Hora fechamento"),
             sg.Input(size=(4,1), key="hf"),
             sg.Text(":"),
             sg.Input(size=(4,1), key="mf")],

            [sg.Push(),
             sg.Button("Salvar"),
             sg.Button("Cancelar")]
        ]

        window = sg.Window("Cadastro de Clínica", layout)
        evento, valores = window.read()
        window.close()

        if evento != "Salvar":
            return None

        return valores

    def selecionar_clinica(self, clinicas):
        
        if len(clinicas) == 0:
            self.mostrar_erro("Nenhuma clínica cadastrada.")
            return None

        dados = []

        for clinica in clinicas:
            dados.append([
                clinica.nome,
                clinica.loc,
                clinica.horario_abertura.strftime("%H:%M"),
                clinica.horario_fechamento.strftime("%H:%M")
            ])

        layout = [

            [sg.Text("Selecione uma clínica")],

            [sg.Table(
                values=dados,
                headings=["Nome", "Localização", "Abre", "Fecha"],
                auto_size_columns=True,
                justification="center",
                num_rows=8,
                key="tabela",
                select_mode=sg.TABLE_SELECT_MODE_BROWSE
            )],

            [sg.Push(),
             sg.Button("Selecionar"),
             sg.Button("Cancelar")]
        ]

        window = sg.Window("Selecionar Clínica", layout)

        evento, valores = window.read()
        window.close()

        if evento != "Selecionar":
            return None

        if not valores["tabela"]:
            return None

        return valores["tabela"][0]

    def mostrar_clinicas(self, clinicas):

        dados = []

        for clinica in clinicas:

            dados.append([
                clinica.nome,
                clinica.loc,
                clinica.descricao,
                clinica.horario_abertura.strftime("%H:%M"),
                clinica.horario_fechamento.strftime("%H:%M")
            ])

        layout = [

            [sg.Table(
                values=dados,
                headings=[
                    "Nome",
                    "Localização",
                    "Descrição",
                    "Abre",
                    "Fecha"
                ],
                auto_size_columns=True,
                justification="center",
                num_rows=10
            )],

            [sg.Push(), sg.Button("Fechar")]
        ]

        window = sg.Window("Lista de Clínicas", layout)

        window.read()
        window.close()
        
    def alterar_dados_clinica(self, clinica):
        layout = [

            [sg.Text("Nome", size=(15,1)),
             sg.Input(default_text=clinica.nome, key="nome")],

            [sg.Text("Localização", size=(15,1)),
             sg.Input(default_text=clinica.loc, key="loc")],

            [sg.Text("Descrição", size=(15,1)),
             sg.Input(default_text=clinica.descricao, key="descricao")],

            [sg.Text("Hora abertura"),
             sg.Input(
                 default_text=clinica.horario_abertura.strftime("%H"),
                 size=(4,1),
                 key="ha"
             ),
             sg.Text(":"),
             sg.Input(
                 default_text=clinica.horario_abertura.strftime("%M"),
                 size=(4,1),
                 key="ma"
             )],

            [sg.Text("Hora fechamento"),
             sg.Input(
                 default_text=clinica.horario_fechamento.strftime("%H"),
                 size=(4,1),
                 key="hf"
             ),
             sg.Text(":"),
             sg.Input(
                 default_text=clinica.horario_fechamento.strftime("%M"),
                 size=(4,1),
                 key="mf"
             )],

            [sg.Button("Salvar"),
             sg.Button("Cancelar")]
        ]

        window = sg.Window("Alterar Clínica", layout)
        evento, valores = window.read()
        window.close()

        if evento != "Salvar":
            return None
        return valores

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem)

    def mostrar_erro(self, mensagem):
        sg.popup_error(mensagem)

    def confirmar_exclusao(self, nome):

        resposta = sg.popup_yes_no(
            f"Deseja realmente excluir a clínica\n\n{nome}?"
        )

        return resposta == "Yes"
