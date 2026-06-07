from atendimento import Atendimento
from telaAtendimento import TelaAtendimento


class ControladorAtendimento:
    def __init__(self):
        self.__atendimentos = []
        self.__tela_atendimento = TelaAtendimento()

    @property
    def atendimentos(self):
        return self.__atendimentos

    def cadastrar_atendimento(self, controlador_clinica, controlador_paciente, controlador_profissional, controlador_tipo_atendimento):
        try:
            clinica = controlador_clinica.escolher_clinica()
            if clinica is None:
                return

            paciente = controlador_paciente.escolher_paciente()
            if paciente is None:
                return

            profissional = controlador_profissional.escolher_profissional()
            if profissional is None:
                return

            tipo_atendimento = controlador_tipo_atendimento.escolher_tipo_atendimento()
            if tipo_atendimento is None:
                return

            data_atendimento = self.__tela_atendimento.ler_data_atendimento()
            horario_inicio = self.__tela_atendimento.ler_horario_inicio()
            horario_fim = self.__tela_atendimento.ler_horario_fim()
            valor = self.__tela_atendimento.ler_valor()

            atendimento = Atendimento(clinica, paciente, profissional, data_atendimento, horario_inicio, horario_fim, tipo_atendimento, valor)

            atendimento.validar_atendimento()
            self.__atendimentos.append(atendimento)

            self.__tela_atendimento.mostrar_mensagem(
                "Atendimento cadastrado com sucesso."
            )

        except ValueError as erro:
            self.__tela_atendimento.mostrar_erro_cadastro(erro)

    def listar_atendimentos(self):
        self.__tela_atendimento.mostrar_atendimentos(self.__atendimentos)

    def escolher_atendimento(self):
        return self.__tela_atendimento.escolher_atendimento(self.__atendimentos)

    def alterar_atendimento(self, controlador_clinica, controlador_paciente, controlador_profissional, controlador_tipo_atendimento):
        atendimento = self.escolher_atendimento()

        if atendimento is None:
            return

        try:
            self.__tela_atendimento.mostrar_inicio_alteracao()

            nova_clinica = controlador_clinica.escolher_clinica()
            if nova_clinica is None:
                return

            novo_paciente = controlador_paciente.escolher_paciente()
            if novo_paciente is None:
                return

            novo_profissional = controlador_profissional.escolher_profissional()
            if novo_profissional is None:
                return

            novo_tipo_atendimento = controlador_tipo_atendimento.escolher_tipo_atendimento()
            if novo_tipo_atendimento is None:
                return

            nova_data = self.__tela_atendimento.ler_data_atendimento()
            novo_horario_inicio = self.__tela_atendimento.ler_horario_inicio()
            novo_horario_fim = self.__tela_atendimento.ler_horario_fim()
            novo_valor = self.__tela_atendimento.ler_valor()

            atendimento.clinica = nova_clinica
            atendimento.paciente = novo_paciente
            atendimento.profissional = novo_profissional
            atendimento.tipo_atendimento = novo_tipo_atendimento
            atendimento.data = nova_data
            atendimento.horario_inicio = novo_horario_inicio
            atendimento.horario_fim = novo_horario_fim
            atendimento.valor = novo_valor

            atendimento.validar_atendimento()

            self.__tela_atendimento.mostrar_mensagem("Atendimento alterado com sucesso.")

        except ValueError as erro:
            self.__tela_atendimento.mostrar_erro_alteracao(erro)

    def excluir_atendimento(self):
        atendimento = self.escolher_atendimento()

        if atendimento is None:
            return

        if self.__tela_atendimento.confirmar_exclusao():
            self.__atendimentos.remove(atendimento)
            self.__tela_atendimento.mostrar_mensagem("Atendimento excluído com sucesso.")
        else:
            self.__tela_atendimento.mostrar_mensagem("Exclusão cancelada.")

    def abrir_menu(self, controlador_clinica, controlador_paciente, controlador_profissional, controlador_tipo_atendimento):
        while True:
            opcao = self.__tela_atendimento.mostrar_menu()

            if opcao == "1":
                self.cadastrar_atendimento(controlador_clinica, controlador_paciente, controlador_profissional, controlador_tipo_atendimento)

            elif opcao == "2":
                self.listar_atendimentos()

            elif opcao == "3":
                self.alterar_atendimento(controlador_clinica, controlador_paciente, controlador_profissional, controlador_tipo_atendimento)

            elif opcao == "4":
                self.excluir_atendimento()

            elif opcao == "0":
                break

            else:
                self.__tela_atendimento.mostrar_mensagem("Opção inválida.")