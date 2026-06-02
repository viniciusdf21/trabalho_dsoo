from pessoa import Pessoa


class Paciente(Pessoa):
    def __init__(self, nome, cpf, telefone, data_nascimento):
        super().__init__(nome, cpf, telefone)
        self.__data_nascimento = data_nascimento

    @property
    def data_nascimento(self):
        return self.__data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, nova_data):
        self.__data_nascimento = nova_data
