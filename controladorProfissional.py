from profissional import Profissional
from telaProfissionalGUI import TelaProfissional
from DAO.profissionalDAO import ProfissionalDAO

class ControladorProfissional:
    def __init__(self):
        self.__profissionaisDAO = ProfissionalDAO()
        self.__tela = TelaProfissional()

    def cadastrar_profissional(self):
        dados = self.__tela.pegar_dados_profissional()

        if dados is None:
            return

        try: 
            profissional = Profissional(
                dados["nome"],
                dados["cpf"],
                dados["celular"],
                dados["especialidade"],
                dados["registro"]
            )
            self.__profissionaisDAO.add(profissional)
            self.__tela.mostrar_mensagem('Profissional cadastrado com sucesso!')

        except ValueError as erro:
            self.__tela.mostrar_erro(str(erro))

    def listar_profissionais(self):
        profissionais = list(self.__profissionaisDAO.get_all())
        if not profissionais:
            self.__tela.mostrar_erro("Nenhum profissional cadastrado.")
            return

        self.__tela.mostrar_profissionais(profissionais)

    def excluir_profissional(self):
        profissionais = list(self.__profissionaisDAO.get_all())
        indice = self.__tela.selecionar_profissional(profissionais)

        if indice is None:
            return

        profissional = profissionais[indice]
        if self.__tela.confirmar_exclusao(profissional.nome):
            self.__profissionaisDAO.remove(profissional)
            self.__tela.mostrar_mensagem("Profissional removido com sucesso.")

    def alterar_profissional(self):
        profissionais = list(self.__profissionaisDAO.get_all())
        indice = self.__tela.selecionar_profissional(profissionais)

        if indice is None:
            return

        profissional = profissionais[indice]
        dados = self.__tela.alterar_profissional(profissional)
        
        if dados is None:
            return

        try:
            profissional.nome = dados["nome"]
            profissional.celular = dados["celular"]
            profissional.especialidade = dados["especialidade"]
            profissional.registro = dados["registro"]

            self.__profissionaisDAO.update(profissional)
            self.__tela.mostrar_mensagem("Profissional alterado com sucesso!")

        except ValueError as erro:
            self.__tela.mostrar_erro(str(erro))

    def escolher_profissional(self):
        profissionais = list(self.__profissionaisDAO.get_all())
        indice = self.__tela.selecionar_profissional(profissionais)

        if indice is None:
            return None

        return self.__profissionais[indice]

    def abrir_menu(self):
        while True:

            opcao = self.__tela.mostrar_menu()

            if opcao == "1":
                self.cadastrar_profissional()

            elif opcao == "2":
                self.listar_profissionais()

            elif opcao == "3":
                self.excluir_profissional()

            elif opcao == "4":
                self.alterar_profissional()

            elif opcao == "0":
                break
