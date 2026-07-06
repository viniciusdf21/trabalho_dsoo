from tipoAtendimento import TipoAtendimento
from telaTipoAtendimentoGUI import TelaTipoAtendimento
from DAO.tipoAtendimentoDAO import TipoAtendimentoDAO

class ControladorTipoAtendimentos:
    def __init__(self):
        self.__tiposDAO = TipoAtendimentoDAO()
        self.__tela = TelaTipoAtendimento()

    def cadastrar_tipo_atendimento(self):
        dados = self.__tela.pegar_dados_tipo()

        if dados is None:
            return

        try:
            tipo = TipoAtendimento(dados["nome"], dados["descricao"], float(dados["valor"]))
            self.__tiposDAO.add(tipo)
            self.__tela.mostrar_mensagem("Tipo de atendimento cadastrado com sucesso!")

        except ValueError: 
            self.__tela.mostrar_erro("Digite um valor numérico válido")

    def listar_tipos_atendimento(self):
        tipos = list(self.__tiposDAO.get_all())
        if not self.__tipos_atendimento:
            self.__tela.mostrar_erro("Nenhum tipo de atendimento cadastrado.")
            return

        self.__tela.mostrar_tipos_atendimento(tipos)

    def excluir_tipo_atendimento(self):
        indice = self.__tela.selecionar_tipo(self.__tipos_atendimento)

        if indice is None:
            return

        tipo = tipos[indice]
        
        if self.__tela.confirmar_exclusao(tipo.nome):
            self.__tiposDAO.remove(tipo)
            self.__tela.mostrar_mensagem("Tipo de atendimento removido com sucesso!")
            
    def alterar_tipo_atendimento(self):
        tipos = list(self.__tiposDAO.get_all())
        indice = self.__tela.selecionar_tipo(tipos)

        if indice is None:
            return

        tipo = tipos[indice]
        dados = self.__tela.alterar_tipo(tipo)

        if dados is None:
            return

        try:
            tipo.nome = dados["nome"]
            tipo.descricao = dados["descricao"]
            tipo.valor_base = float(dados["valor"])
            self.__tiposDAO.update(tipo)
            self.__tela.mostrar_mensagem("Tipo de atendimento alterado com sucesso!")

        except ValueError:
            self.__tela.mostrar_erro("Valor inválido.")

    def escolher_tipo_atendimento(self):
        tipos = list(self.__tiposDAO.get_all())
        indice = self.__tela.selecionar_tipo(tipos)

        if indice is None:
            return None

        return tipos[indice]

    def abrir_menu(self):
        while True:

            opcao = self.__tela.mostrar_menu()

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
