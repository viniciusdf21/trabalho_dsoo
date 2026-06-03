from pagamento import Pagamento


class CartaoCredito(Pagamento):
    def __init__(self, data_pagamento, atendimento, paciente: Paciente, valor_pago, numero, bandeira):
        super().__init__(data_pagamento, atendimento, paciente, valor_pago)
        self.__numero = numero
        self.__bandeira = bandeira
    
    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def bandeira(self):
        return self.__bandeira

    @bandeira.setter
    def bandeira(self, bandeira):
        self.__bandeira = bandeira
