from abc import ABC


class Pagamento(ABC):
    def __init__(self, data_pagamento, atendimento, paciente, valor_pago):
        self.__data = data_pagamento
        self.__atendimento = atendimento
        self.__paciente = paciente
        self.__valor_pago = valor_pago
    
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def atendimento(self):
        return self.__atendimento

    @atendimento.setter
    def atendimento(self, atendimento):
        self.__atendimento = atendimento

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente):
        self.__paciente = paciente

    @property
    def valor_pago(self):
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, valor_pago):
        self.__valor_pago = valor_pago


    def validar_pagamento(self):
        if self.__valor_pago <= 0:
            raise ValueError("O valor pago deve ser maior que zero")

        return True

    def registrar_pagamento(self):
        self.validar_pagamento()