from abc import ABC


class Pagamento(ABC):
    def __init__(self, data_pagamento, atendimento, paciente, valor_pago):
        self.__data = data_pagamento
        self.__atendimento = atendimento
        self.__paciente = paciente
        self.__valor_pago = valor_pago
