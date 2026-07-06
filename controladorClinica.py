from clinica import Clinica
from datetime import time
from telaClinicaGUI import TelaClinica
from DAO.clinicaDAO import ClinicaDAO

class ControladorClinica:
    def __init__(self):
        self.__clinicasDAO = ClinicaDAO()
        self.__tela = TelaClinica()

    def cadastrar_clinica(self):
        dados = self.__tela.pegar_dados_clinica()

        if dados is None:
            return

        try:
            abertura = time(int(dados["ha"]), int(dados["ma"]))
            fechamento = time(int(dados["hf"]), int(dados["mf"]))

            clinica = Clinica(
                dados["nome"],
                dados["loc"],
                dados["descricao"],
                abertura,
                fechamento
            )
            self.__clinicasDAO.add(clinica)
            self.__tela.mostrar_mensagem("Clínica cadastrada com sucesso!")
            
        except ValueError:
            self.__tela.mostrar_erro("Horário inválido. Tente novamente.")
    
    def exibir_clinica(self):
        clinicas = list(self.__clinicasDAO.get_all())
        if len(clinicas) == 0:
            self.__tela.mostrar_erro("Nenhuma clínica cadastrada.")
            return

        self.__tela.mostrar_clinicas(clinicas)

    def excluir_clinica(self):
        clinicas = list(self.__clinicasDAO.get_all())
        indice = self.__tela.selecionar_clinica(clinicas)

        if indice is None:
            return

        clinica = clinicas[indice]
        if self.__tela.confirmar_exclusao(clinica.nome):
            self.__clinicasDAO.remove(clinica)
            self.__tela.mostrar_mensagem("Clínica removida com sucesso!")
    
    def alterar_clinica(self):
        clinicas = list(self.__clinicasDAO.get_all())
        indice = self.__tela.selecionar_clinica(clinicas)
        
        if indice is None:
            return

        clinica = clinicas[indice]
        dados = self.__tela.alterar_dados_clinica(clinica)

        if dados is None:
            return

        try:

            clinica.nome = dados["nome"]
            clinica.loc = dados["loc"]
            clinica.descricao = dados["descricao"]
            clinica.horario_abertura = time(int(dados["ha"]), int(dados["ma"]))
            clinica.horario_fechamento = time(int(dados["hf"]), int(dados["mf"]))
            clinicas = list(self.__clinicasDAO.get_all())
            self.__tela.mostrar_mensagem("Clínica alterada com sucesso!")

        except ValueError:

            self.__tela.mostrar_erro("Clínica não encontrada.")

    def escolher_clinica(self):
        clinicas = list(self.__clinicasDAO.get_all())
        indice = self.__tela.selecionar_clinica(clinicas)

        if indice is None:
            return None
        return clinicas[indice]

    def abrir_menu(self):
        while True:

            opcao = self.__tela.mostrar_menu()

            if opcao == "1":
                self.cadastrar_clinica()

            elif opcao == "2":
                self.exibir_clinica()

            elif opcao == "3":
                self.alterar_clinica()

            elif opcao == "4":
                self.excluir_clinica()

            elif opcao == "0":
                break
