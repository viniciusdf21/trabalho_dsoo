from pesssoa import Pessoa


class Profissional(Pessoa):
    def __init__(self, nome, cpf, celular, especialidade, registro):
        super().__init__(nome, cpf, celular)
        self.__especialidade = especialidade
        self.__registro = registro
