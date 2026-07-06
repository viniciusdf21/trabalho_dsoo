from datetime import date, time
import FreeSimpleGUI as sg


class TelaAtendimento:
    def __init__(self):
        self.__window = None
        self.__horario_fim = None


    def mostrar_menu(self):
        layout = [
            [sg.Text("ATENDIMENTOS")],
            [sg.Button("Cadastrar", key="1", size=(25, 2))],
            [sg.Button("Listar", key="2", size=(25, 2))],
            [sg.Button("Alterar", key="3", size=(25, 2))],
            [sg.Button("Excluir", key="4", size=(25, 2))],
            [sg.Button("Voltar", key="0", size=(25, 2))]
        ]

        self.__window = sg.Window("Menu Atendimentos", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento == sg.WINDOW_CLOSED:
            return "0"

        return evento


    def ler_data_atendimento(self):
        layout = [
            [sg.Text("DATA DO ATENDIMENTO")],
            [sg.Text("Dia:"), sg.Input(key="dia", size=(10, 1))],
            [sg.Text("Mês:"), sg.Input(key="mes", size=(10, 1))],
            [sg.Text("Ano:"), sg.Input(key="ano", size=(10, 1))],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        self.__window = sg.Window("Data do Atendimento", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento in (sg.WINDOW_CLOSED, "Cancelar"):
            raise ValueError("Operação cancelada.")

        try:
            dia = int(valores["dia"])
            mes = int(valores["mes"])
            ano = int(valores["ano"])

            return date(ano, mes, dia)

        except ValueError:
            raise ValueError("Data inválida.")


    def ler_horario_inicio(self):
        layout = [
            [sg.Text("HORÁRIO DO ATENDIMENTO")],
            [sg.Text("Hora de início:"), sg.Input(key="hora_inicio", size=(10, 1))],
            [sg.Text("Minuto de início:"), sg.Input(key="minuto_inicio", size=(10, 1))],
            [sg.Text("Hora de fim:"), sg.Input(key="hora_fim", size=(10, 1))],
            [sg.Text("Minuto de fim:"), sg.Input(key="minuto_fim", size=(10, 1))],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        self.__window = sg.Window("Horário do Atendimento", layout)
        evento, valores = self.__window.read()
        self.__window.close()

        if evento in (sg.WINDOW_CLOSED, "Cancelar"):
            raise ValueError("Operação cancelada.")

        try:
            horario_inicio = time(
                int(valores["hora_inicio"]),
                int(valores["minuto_inicio"])
            )

            self.__horario_fim = time(
                int(valores["hora_fim"]),
                int(valores["minuto_fim"])
            )

            return horario_inicio

        except ValueError:
            raise ValueError("Horário inválido.")


    def ler_horario_fim(self):
        if self.__horario_fim is None:
            raise ValueError("Horário de fim não informado.")

        horario_fim = self.__horario_fim
        self.__horario_fim = None

        return horario_fim


    def ler_valor(self):
        valor = sg.popup_get_text("Valor do atendimento:")

        if valor is None:
            raise ValueError("Operação cancelada.")

        try:
            valor = float(valor.replace(",", "."))

            if valor <= 0:
                raise ValueError("O valor deve ser maior que zero.")

            return valor

        except ValueError:
            raise ValueError("Valor inválido.")


    def mostrar_inicio_alteracao(self):
        sg.popup("Digite novamente os dados do atendimento.")


    def mostrar_atendimentos(self, atendimentos):
        if not atendimentos:
            sg.popup("Nenhum atendimento cadastrado.")
            return

        dados = []

        for atendimento in atendimentos:
            dados.append([
                atendimento.clinica.nome,
                atendimento.paciente.nome,
                atendimento.profissional.nome,
                atendimento.data,
                atendimento.horario_inicio.strftime("%H:%M"),
                atendimento.horario_fim.strftime("%H:%M"),
                atendimento.tipo_atendimento.nome,
                f"R$ {atendimento.valor:.2f}",
                f"R$ {atendimento.calcular_valor_total():.2f}",
                f"R$ {atendimento.calcular_valor_restante():.2f}"
            ])

        cabecalho = [
            "Clínica",
            "Paciente",
            "Profissional",
            "Data",
            "Início",
            "Fim",
            "Tipo",
            "Valor Base",
            "Valor Total",
            "Valor Restante"
        ]

        layout = [
            [sg.Table(
                values=dados,
                headings=cabecalho,
                auto_size_columns=False,
                col_widths=[12, 12, 12, 12, 8, 8, 14, 12, 12, 14],
                justification="center",
                num_rows=10,
                key="tabela_atendimentos"
            )],
            [sg.Button("Fechar", size=(10, 1))]
        ]

        self.__window = sg.Window("Lista de Atendimentos", layout)
        evento, valores = self.__window.read()
        self.__window.close()

    def escolher_atendimento(self, atendimentos):
        if not atendimentos:
            sg.popup("Nenhum atendimento cadastrado.")
            return None

        opcoes = []

        for i, atendimento in enumerate(atendimentos):
            texto = (
                f"{i + 1} - "
                f"{atendimento.paciente.nome} - "
                f"{atendimento.data} - "
                f"{atendimento.horario_inicio.strftime('%H:%M')}"
            )
            opcoes.append(texto)

        layout = [
            [sg.Text("Escolha um atendimento:")],
            [sg.Listbox(opcoes, size=(55, 8), key="atendimento")],
            [sg.Button("Selecionar", size=(15, 1)), sg.Button("Cancelar", size=(15, 1))]
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
        resposta = sg.popup_yes_no("Deseja realmente excluir este atendimento?")

        return resposta == "Yes"

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem)

    def mostrar_erro_cadastro(self, erro):
        sg.popup(f"Erro ao cadastrar atendimento: {erro}")

    def mostrar_erro_alteracao(self, erro):
        sg.popup(f"Erro ao alterar atendimento: {erro}")
