from telaRelatorioGUI import TelaRelatorio


class ControladorRelatorio:
    def __init__(self):
        self.__tela_relatorio = TelaRelatorio()


    def relatorio_atendimento_mais_caro_barato(self, controlador_atendimento):
        atendimentos = controlador_atendimento.atendimentos

        if not atendimentos:
            self.__tela_relatorio.mostrar_mensagem("Nenhum atendimento cadastrado.")
            return

        atendimento_mais_caro = atendimentos[0]
        atendimento_mais_barato = atendimentos[0]

        for atendimento in atendimentos:
            if atendimento.calcular_valor_total() > atendimento_mais_caro.calcular_valor_total():
                atendimento_mais_caro = atendimento

            if atendimento.calcular_valor_total() < atendimento_mais_barato.calcular_valor_total():
                atendimento_mais_barato = atendimento

        self.__tela_relatorio.mostrar_relatorio_atendimento_mais_caro_barato(
            atendimento_mais_caro,
            atendimento_mais_barato
        )


    def abrir_menu(self, controlador_atendimento):
        while True:
            opcao = self.__tela_relatorio.mostrar_menu()

            if opcao == "1":
                self.relatorio_atendimento_mais_caro_barato(controlador_atendimento)

            elif opcao == "0":
                break

            else:
                self.__tela_relatorio.mostrar_mensagem("Opção inválida.")