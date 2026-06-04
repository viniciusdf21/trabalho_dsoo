from controladorPaciente import ControladorPaciente
from controladorProfissional import ControladorProfissional
from controladorClinica import ControladorClinica
from controladorTipoAten import ControladorTipoAtendimentos

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
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.__controladorPaciente.abrir_menu()
                
            elif opcao == "2":
                self.__controlador_profissionais.abrir_menu()

            elif opcao == "3":
                self.__controlador_clinica.abrir_menu()

            elif opcao == "4":
                self.__controlador_tipo_atendimentos.abrir_menu()

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")
