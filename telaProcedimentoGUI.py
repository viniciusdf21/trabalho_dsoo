import FreeSimpleGUI as sg


class TelaProcedimento:
    def __init__(self):
        self.__window = None


    def mostrar_menu(self):
        layout = [
            [sg.Text("PROCEDIMENTOS")],
            [sg.Button("Registrar", key="1", size=(25, 2))],
            [sg.Button("Listar", key="2", size=(25, 2))],
            [sg.Button("Alterar", key="3", size=(25, 2))],
            [sg.Button("Excluir", key="4", size=(25, 2))],
            [sg.Button("Voltar", key="0", size=(25, 2))]
        ]

        self.__window = sg.Window("Menu Procedimentos", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento == sg.WINDOW_CLOSED:
            return "0"

        return evento


    def ler_nome(self):
        nome = sg.popup_get_text("Nome do procedimento:")

        if nome is None:
            raise ValueError("Operação cancelada.")

        nome = nome.strip()

        if nome == "":
            raise ValueError("O nome do procedimento não pode ser vazio.")

        return nome


    def ler_descricao(self):
        descricao = sg.popup_get_text("Descrição do procedimento:")

        if descricao is None:
            raise ValueError("Operação cancelada.")

        descricao = descricao.strip()

        if descricao == "":
            raise ValueError("A descrição do procedimento não pode ser vazia.")

        return descricao


    def ler_custo(self):
        custo = sg.popup_get_text("Custo do procedimento:")

        if custo is None:
            raise ValueError("Operação cancelada.")

        try:
            custo = float(custo.replace(",", "."))

            if custo <= 0:
                raise ValueError("O custo deve ser maior que zero.")

            return custo

        except ValueError:
            raise ValueError("Custo inválido.")

    def mostrar_inicio_alteracao(self):
        sg.popup("Digite novamente os dados do procedimento.")

    def mostrar_procedimentos(self, atendimento):
        if not atendimento.lista_procedimentos:
            sg.popup("Nenhum procedimento registrado.")
            return

        texto = ""

        for procedimento in atendimento.lista_procedimentos:
            texto += procedimento.exibir_dados()
            texto += "\n\n-----------------------------\n\n"

        sg.popup_scrolled(
            texto,
            title="Procedimentos registrados",
            size=(70, 20)
        )

    def escolher_procedimento(self, atendimento):
        if not atendimento.lista_procedimentos:
            sg.popup("Nenhum procedimento registrado.")
            return None

        opcoes = []

        for i, procedimento in enumerate(atendimento.lista_procedimentos):
            texto = f"{i + 1} - {procedimento.nome} - R$ {procedimento.custo:.2f}"
            opcoes.append(texto)

        layout = [
            [sg.Text("Escolha um procedimento:")],
            [sg.Listbox(opcoes, size=(50, 8), key="procedimento")],
            [sg.Button("Selecionar", size=(15, 1)), sg.Button("Cancelar", size=(15, 1))]
        ]

        self.__window = sg.Window("Escolher Procedimento", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento in (sg.WINDOW_CLOSED, "Cancelar"):
            return None

        if not valores["procedimento"]:
            sg.popup("Selecione um procedimento.")
            return None

        escolhido = valores["procedimento"][0]
        indice = opcoes.index(escolhido)

        return atendimento.lista_procedimentos[indice]

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem)

    def mostrar_erro_registro(self, erro):
        sg.popup(f"Erro ao registrar procedimento: {erro}")

    def mostrar_erro_cadastro(self, erro):
        sg.popup(f"Erro ao cadastrar procedimento: {erro}")

    def mostrar_erro_alteracao(self, erro):
        sg.popup(f"Erro ao alterar procedimento: {erro}")
