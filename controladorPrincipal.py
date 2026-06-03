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
            print("4 - Atendimentos")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "0":
                break
