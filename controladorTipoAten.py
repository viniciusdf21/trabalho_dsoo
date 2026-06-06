from tipoAtendimento import TipoAtendimento

class ControladorTipoAtendimentos:
    def __init__(self):
        self.__tipos_atendimento = []

    def cadastrar_tipo_atendimento(self):
        nome = input("Nome do tipo de atendimento: ")
        descricao = input("Descrição: ")

        while True:
            try:
                valor_base = float(input("Valor base: R$ "))
                break

            except ValueError: 
                print("Digite um valor numérico válido")

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

    def excluir_tipo_atendimento(self):
        nome = input("Nome do tipo de atendimento: ")

        for tipo in self.__tipos_atendimento:
            if tipo.nome == nome:
                self.__tipos_atendimento.remove(tipo)
                print("Tipo de atendimento removido com sucesso!")
                return

        print("Tipo de atendimento não encontrado.")
        
    def alterar_tipo_atendimento(self):
        nome = input("Nome do tipo de atendimento: ")

        for tipo in self.__tipos_atendimento:
            if tipo.nome == nome:

                tipo.nome = input("Novo nome: ")
                tipo.descricao = input("Nova descrição: ")

                while True:
                    try:
                        tipo.valor_base = float(input("Novo valor base: R$ "))
                        break

                    except ValueError:
                        print("Digite um valor numérico válido.")

                print("Tipo de atendimento alterado com sucesso!")
                return

        print("Tipo de atendimento não encontrado.")
        
    def escolher_tipo_atendimento(self):
        if len(self.__tipo_atendimentos) == 0:
            print("Nenhum tipo de atendimento cadastrado.")
            return None

        print("\n=== ESCOLHER TIPO DE ATENDIMENTO ===")

        for i, tipo_atendimento in enumerate(self.__tipo_atendimentos):
            print(f"{i + 1} - {tipo_atendimento.nome}")

        try:
            opcao = int(input("Escolha o tipo de atendimento: "))

            if opcao < 1 or opcao > len(self.__tipo_atendimentos):
                print("Opção inválida.")
                return None

            return self.__tipo_atendimentos[opcao - 1]

        except ValueError:
            print("Digite um número válido.")
            return None

    def abrir_menu(self):
        while True:
            print("\n=== TIPOS DE ATENDIMENTO ===")
            print("1 - Cadastrar")
            print("2 - Listar")
            print("3 - Excluir")
            print("4 - Alterar")
            print("0 - Voltar")

            opcao = input("Opção: ")

            if opcao == "1":
                self.cadastrar_tipo_atendimento()

            elif opcao == "2":
                self.listar_tipos_atendimento()

            elif opcao == "3":
                self.excluir_tipo_atendimento()

            elif opcao == "4":
                self.alterar_tipo_atendimento()

            elif opcao == "0":
                break
