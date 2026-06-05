from abc import ABC, abstractmethod


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
        if not self.validar_cpf(novo_cpf):
            raise ValueError("CPF deve conter exatamente 11 dígitos.")
        self.__cpf = novo_cpf
        
    @property
    def celular(self):
        return self.__celular
    
    @celular.setter
    def celular(self, novo_celular):
        self.__celular = novo_celular
        
    def validar_cpf(self, cpf):
        cpf = str(cpf)
        return cpf.isdigit() and len(cpf) == 11
        
    @abstractmethod
    def exibir_dados():
        pass
