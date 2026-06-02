from pesssoa import Pessoa


class Profissional(Pessoa):
    def __init__(self, nome, cpf, celular, especialidade, registro):
        super().__init__(nome, cpf, celular)
        self.__especialidade = especialidade
        self.__registro = registro

    @property
    def especialidade(self):
        return self.__especialidade
    
    @especialidade.setter
    def especialidade(self, nova_esp):
        self.__especialidade = nova_esp
        
    @property
    def registro(self):
        return self.__registro
    
    @registro.setter
    def registro(self, novo_reg):
        self.__registro = novo_reg
        
    def exibir_especialidade(self):
        return f"Especialidade: {self.__especialidade}"
