from pagamento import Pagamento


class CartaoCredito(Pagamento):
    def __init__(self, data_pagamento, atendimento, paciente: Paciente, valor_pago, numero, bandeira):
        super().__init__(data_pagamento, atendimento, paciente, valor_pago)
        self.__numero = numero
        self.__bandeira = bandeira
