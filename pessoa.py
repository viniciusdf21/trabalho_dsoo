from ABC import ABC


class Pessoa(ABC):
    def __init__(self, nome, cpf, celular):
        self.__nome = nome
        self.__cpf = cpf
        self.__celular = celular

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
        
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf
        
    @property
    def celular(self):
        return self.__celular
    
    @celular.setter
    def celular(self, novo_celular):
        self.__celular = novo_celular
        
    def validar_cpf():
        # implementacao
        pass
        
    @abstractmethod
    def exibir_dados():
        pass
