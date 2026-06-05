from pagamento import Pagamento


class CartaoCredito(Pagamento):
    def __init__(self, data_pagamento, atendimento, paciente, valor_pago, numero, bandeira):
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

    def validar_cartao(self):
        numero = self.__numero
        if len(numero) < 13 or not numero.isdigit():
            raise ValueError("Número do cartão inválido")
        if self.__bandeira == "":
            raise ValueError("Bandeira do cartão inválida")
        return True
    
    def validar_pagamento(self):
        if self.valor_pago <= 0:
            raise ValueError("O valor pago deve ser maior que zero")
        return self.validar_cartao()