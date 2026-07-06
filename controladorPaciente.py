from paciente import Paciente
from datetime import date
from telaPacienteGUI import TelaPaciente
from DAO.pacienteDAO import PacienteDAO


class ControladorPaciente:
    def __init__(self):
        self.__pacientesDAO = PacienteDAO()
        self.__tela = TelaPaciente()

    def cadastrar_paciente(self):
        dados = self.__tela.pegar_dados_paciente()
        if dados is None:
            return

        try:
            data = date(int(dados["ano"]), int(dados["mes"]), int(dados["dia"]))
            paciente = Paciente(dados["nome"], dados["cpf"], dados["celular"], data)

            self.__pacientesDAO.add(paciente)
            self.__tela.mostrar_mensagem("Paciente cadastrado com sucesso!")

        except ValueError: 
            self.__tela.mostrar_erro("Data inválida. Tente Novamente.") 

    def listar_pacientes(self):
        pacientes = list(self.__pacientesDAO.get_all())
        if len(pacientes) == 0:
            self.__tela.mostrar_erro("Nenhum paciente cadastrado.")
            return

        self.__tela.mostrar_pacientes(pacientes)

    def excluir_paciente(self):
        pacientes = list(self.__pacientesDAO.get_all())
        indice = self.__tela.selecionar_paciente(pacientes)
        if indice is None:
            return

        paciente = pacientes[indice]

        if self.__tela.confirmar_exclusao(paciente.nome):
            self.__pacientesDAO.remove(paciente)
            self.__tela.mostrar_mensagem("Paciente removido com sucesso!")

    def alterar_paciente(self):
        pacientes = list(self.__pacientesDAO.get_all())
        indice = self.__tela.selecionar_paciente(pacientes)

        if indice is None:
            return

        paciente = pacientes[indice]
        dados = self.__tela.alterar_paciente(paciente)

        if dados is None:
            return

        try:
            paciente.nome = dados["nome"]
            paciente.celular = dados["celular"]

            self.__pacientesDAO.update(paciente)
            self.__tela.mostrar_mensagem("Paciente alterado com sucesso!")

        except ValueError:
            self.__tela.mostrar_erro("Data inválida.")

    def escolher_paciente(self):
        pacientes = list(self.__pacientesDAO.get_all())
        indice = self.__tela.selecionar_paciente(pacientes)

        if indice is None:
            return None

        return pacientes[indice]

    def abrir_menu(self):
        while True:

            opcao = self.__tela.mostrar_menu()

            if opcao == "1":
                self.cadastrar_paciente()

            elif opcao == "2":
                self.listar_pacientes()

            elif opcao == "3":
                self.alterar_paciente()

            elif opcao == "4":
                self.excluir_paciente()

            elif opcao == "0":
                break
