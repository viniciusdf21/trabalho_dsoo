from controladorPaciente import ControladorPaciente
from controladorProfissional import ControladorProfissional
from controladorClinica import ControladorClinica
from controladorTipoAten import ControladorTipoAtendimentos
from controladorAtendimento import ControladorAtendimento
from controladorPagamento import ControladorPagamento
from controladorProcedimento import ControladorProcedimento

class ControladorPrincipal:

    def __init__(self):
        self.__controladorPaciente = ControladorPaciente()
        self.__controladorProfissional = ControladorProfissional()
        self.__controladorClinica = ControladorClinica()
        self.__controladorTipoAtendimentos = ControladorTipoAtendimentos()
        self.__controladorAtendimento = ControladorAtendimento()
        self.__controladorPagamento = ControladorPagamento()
        self.__controladorProcedimento = ControladorProcedimento()

    def relatorio_clinica_mais_atendimentos(self):
        atendimentos = self.__controladorAtendimento.atendimentos
        if len(atendimentos) == 0:
            print("Nenhum atendimento cadastrado.")
            return
        contagem = {}

        for atendimento in atendimentos:
            nome_clinica = atendimento.clinica.nome
            if nome_clinica in contagem:
                contagem[nome_clinica] += 1
            else:
                contagem[nome_clinica] = 1
        maior_clinica = max(contagem, key=contagem.get)

        print("\n=== RELATÓRIO ===")
        print(f"Clínica com mais atendimentos: {maior_clinica}")
        print(f"Quantidade de atendimentos: {contagem[maior_clinica]}")

    def menu_relatorios(self):
        while True:
            print("\n=== RELATÓRIOS ===")
            print("1 - Clínica com mais atendimentos")
            print("0 - Voltar")

            opcao = input("Opção: ")
            if opcao == "1":
                self.relatorio_clinica_mais_atendimentos()

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")


    def iniciar(self):
        while True:
            print("\n=== SISTEMA DA CLÍNICA ===")
            print("1 - Pacientes")
            print("2 - Profissionais")
            print("3 - Clínica")
            print("4 - Tipos de atendimentos")
            print("5 - Atendimentos") 
            print("6 - Pagamentos")
            print("7 - Procedimentos")
            print("8 - Relatórios")
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
                self.menu_relatorios()

            elif opcao == "0":
                print("Sistema encerrado.") 
                break

            else:
                print("Opção inválida.")
