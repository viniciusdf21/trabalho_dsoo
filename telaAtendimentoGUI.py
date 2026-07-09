from datetime import date, time
import FreeSimpleGUI as sg


class TelaAtendimento:
    def __init__(self):
        self.__window = None


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
        dia = sg.popup_get_text("Dia do atendimento:")
        mes = sg.popup_get_text("Mês do atendimento:")
        ano = sg.popup_get_text("Ano do atendimento:")

        if dia is None or mes is None or ano is None:
            raise ValueError("Operação cancelada.")

        try:
            return date(int(ano), int(mes), int(dia))

        except ValueError:
            raise ValueError("Data inválida.")


    def ler_horario_inicio(self):
        hora = sg.popup_get_text("Hora de início:")
        minuto = sg.popup_get_text("Minuto de início:")

        if hora is None or minuto is None:
            raise ValueError("Operação cancelada.")

        try:
            return time(int(hora), int(minuto))

        except ValueError:
            raise ValueError("Horário de início inválido.")


    def ler_horario_fim(self):
        hora = sg.popup_get_text("Hora de fim:")
        minuto = sg.popup_get_text("Minuto de fim:")

        if hora is None or minuto is None:
            raise ValueError("Operação cancelada.")

        try:
            return time(int(hora), int(minuto))

        except ValueError:
            raise ValueError("Horário de fim inválido.")


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

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem)

    def mostrar_erro_cadastro(self, erro):
        sg.popup(f"Erro ao cadastrar atendimento: {erro}")

    def mostrar_erro_alteracao(self, erro):
        sg.popup(f"Erro ao alterar atendimento: {erro}")
