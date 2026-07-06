from controladorPaciente import ControladorPaciente
from controladorProfissional import ControladorProfissional
from controladorClinica import ControladorClinica
from controladorTipoAten import ControladorTipoAtendimentos
from controladorAtendimento import ControladorAtendimento
from controladorPagamento import ControladorPagamento
from controladorProcedimento import ControladorProcedimento
from controladorRelatorio import ControladorRelatorio
from telaPrincipalGUI import TelaPrincipal

class ControladorPrincipal:

    def __init__(self):
        self.__controladorPaciente = ControladorPaciente()
        self.__controladorProfissional = ControladorProfissional()
        self.__controladorClinica = ControladorClinica()
        self.__controladorTipoAtendimentos = ControladorTipoAtendimentos()
        self.__controladorAtendimento = ControladorAtendimento()
        self.__controladorPagamento = ControladorPagamento()
        self.__controladorProcedimento = ControladorProcedimento()
        self.__controladorRelatorio = ControladorRelatorio()
        self.__tela = TelaPrincipal()

    def iniciar(self):
        while True:

            opcao = self.__tela.mostrar_menu()

            if opcao == '1':
                self.__controladorPaciente.abrir_menu()
                
            elif opcao == "2":
                self.__controladorProfissional.abrir_menu()

            elif opcao == "3":
                self.__controladorClinica.abrir_menu()

            elif opcao == "4":
                self.__controladorTipoAtendimentos.abrir_menu()

            elif opcao == "5":
                self.__controladorAtendimento.abrir_menu(
                self.__controladorClinica,
                self.__controladorPaciente,
                self.__controladorProfissional,
                self.__controladorTipoAtendimentos
                )

            elif opcao == "6":
                self.__controladorPagamento.abrir_menu(
                self.__controladorAtendimento
                )

            elif opcao == "7":
                self.__controladorProcedimento.abrir_menu(
                self.__controladorAtendimento
                )

            elif opcao == "8":
                self.__controladorRelatorio.abrir_menu(self.__controladorAtendimento)

            elif opcao == "0":
                self.__tela.mostrar_mensagem("Sistema encerrado.") 
                break

            else:
                print("Opção inválida.")
