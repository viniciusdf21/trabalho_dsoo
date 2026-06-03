from tipoAtendimento import TipoAtendimento

class ControladorTipoAtendimentos:
    def __init__(self):
        self.__tipos_atendimento = []

    def cadastrar_tipo_atendimento(self):
        nome = input("Nome do tipo de atendimento: ")
        descricao = input("Descrição: ")
        valor_base = float(input("Valor base: R$ "))

        tipo = TipoAtendimento(nome, descricao, valor_base)
        self.__tipos_atendimento.append(tipo)

        print("Tipo de atendimento cadastrado com sucesso!")

    def listar_tipos_atendimento(self):
        if not self.__tipos_atendimento:
            print("Nenhum tipo de atendimento cadastrado.")
            return

        for tipo in self.__tipos_atendimento:
            print("\n------------------")
            print(tipo.exibir_dados())

    def abrir_menu(self):
        while True:
            print("\n=== TIPOS DE ATENDIMENTO ===")
            print("1 - Cadastrar")
            print("2 - Listar")
            print("0 - Voltar")

            opcao = input("Opção: ")

            if opcao == "1":
                self.cadastrar_tipo_atendimento()

            elif opcao == "2":
                self.listar_tipos_atendimento()

            elif opcao == "0":
                break
