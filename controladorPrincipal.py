from controladorPaciente import ControladorPaciente
from controladorProfissional import ControladorProfissional
from controladorClinica import ControladorClinica
from controladorTipoAten import ControladorTipoAtendimentos
from controladorAtendimento import ControladorAtendimento

class ControladorPrincipal:

    def __init__(self):
        pass

    def iniciar(self):
        while True:
            print("\n=== SISTEMA DA CLÍNICA ===")
            print("1 - Pacientes")
            print("2 - Profissionais")
            print("3 - Clínica")
            print("4 - Tipos de atendimentos")
            print("5 - Atendimentos") 
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.__controladorPaciente.abrir_menu()
                
            elif opcao == "2":
                self.__controladorProfissional.abrir_menu()

            elif opcao == "3":
                self.__controladorClinica.abrir_menu()

            elif opcao == "4":
                self.__controladorTipoAtendimentos.abrir_menu()

            elif opcao == "5":
                self.__controladorAtendimento.abrir_menu()

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")
