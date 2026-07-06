from procedimento import Procedimento
from telaProcedimentoGUI import TelaProcedimento


class ControladorProcedimento:
    def __init__(self):
        self.__tela_procedimento = TelaProcedimento()


    def registrar_procedimento(self, atendimento, procedimento: Procedimento, controlador_atendimento):
        try:
            atendimento.adicionar_procedimento(procedimento)
            controlador_atendimento.atualizar_atendimento(atendimento)
            self.__tela_procedimento.mostrar_mensagem("Procedimento registrado com sucesso.")
            return procedimento

        except ValueError as erro:
            self.__tela_procedimento.mostrar_erro_registro(erro)
            return None


    def cadastrar_procedimento(self, atendimento, controlador_atendimento):
        try:
            nome = self.__tela_procedimento.ler_nome()
            descricao = self.__tela_procedimento.ler_descricao()
            custo = self.__tela_procedimento.ler_custo()
            procedimento = Procedimento(nome, descricao, custo, atendimento.profissional)
            self.registrar_procedimento(atendimento, procedimento, controlador_atendimento)

        except ValueError as erro:
            self.__tela_procedimento.mostrar_erro_cadastro(erro)


    def listar_procedimentos(self, atendimento):
        self.__tela_procedimento.mostrar_procedimentos(atendimento)


    def escolher_procedimento(self, atendimento):
        return self.__tela_procedimento.escolher_procedimento(atendimento)


    def alterar_procedimento(self, atendimento, controlador_atendimento):
        procedimento = self.escolher_procedimento(atendimento)

        if procedimento is None:
            return

        try:
            self.__tela_procedimento.mostrar_inicio_alteracao()

            novo_nome = self.__tela_procedimento.ler_nome()
            nova_descricao = self.__tela_procedimento.ler_descricao()
            novo_custo = self.__tela_procedimento.ler_custo()

            procedimento.nome = novo_nome
            procedimento.descricao = nova_descricao
            procedimento.custo = novo_custo

            controlador_atendimento.atualizar_atendimento(atendimento)

            self.__tela_procedimento.mostrar_mensagem("Procedimento alterado com sucesso.")

        except ValueError as erro:
            self.__tela_procedimento.mostrar_erro_alteracao(erro)


    def excluir_procedimento(self, atendimento, controlador_atendimento):
        procedimento = self.escolher_procedimento(atendimento)

        if procedimento is None:
            return

        atendimento.lista_procedimentos.remove(procedimento)
        controlador_atendimento.atualizar_atendimento(atendimento)

        self.__tela_procedimento.mostrar_mensagem("Procedimento excluído com sucesso.")


    def abrir_menu(self, controlador_atendimento):
        while True:
            opcao = self.__tela_procedimento.mostrar_menu()

            if opcao == "1":
                atendimento = controlador_atendimento.escolher_atendimento()

                if atendimento is not None:
                    self.cadastrar_procedimento(atendimento, controlador_atendimento)

            elif opcao == "2":
                atendimento = controlador_atendimento.escolher_atendimento()

                if atendimento is not None:
                    self.listar_procedimentos(atendimento)

            elif opcao == "3":
                atendimento = controlador_atendimento.escolher_atendimento()

                if atendimento is not None:
                    self.alterar_procedimento(atendimento, controlador_atendimento)

            elif opcao == "4":
                atendimento = controlador_atendimento.escolher_atendimento()

                if atendimento is not None:
                    self.excluir_procedimento(atendimento, controlador_atendimento)

            elif opcao == "0":
                break

            else:
                self.__tela_procedimento.mostrar_mensagem("Opção inválida.")
