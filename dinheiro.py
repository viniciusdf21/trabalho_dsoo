from pagamento import Pagamento


class Dinheiro(Pagamento):
    def __init__(self, data_pag, atendimento, paciente, valor_pago):
        super().__init__(data_pag, atendimento, paciente, valor_pago)
    
    def validar_pagamento(self):
        if self.valor_pago <= 0:
            raise ValueError("O valor pago deve ser maior que zero")
        return True
