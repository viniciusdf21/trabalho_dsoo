from pagamento import Pagamento


class Pix(Pagamento):
    def __init__(self, data_pag, atendimento, paciente, valor_pago, cpf_pagante):
        super().__init__(data_pag, atendimento, paciente, valor_pago)
        self.__cpf_pagante = cpf_pagante

    @property
    def cpf_pagante(self):
        return self.__cpf_pagante

    @cpf_pagante.setter
    def cpf_pagante(self, cpf_pagante):
        self.__cpf_pagante = cpf_pagante

    def validar_cpf(self):
        cpf = self.__cpf_pagante
        if len(cpf) == 11:
            return True
        else:
            raise ValueError("CPF deve possuir 11 dígitos")

    def validar_pagamento(self):
        if self.valor_pago <= 0:
            raise ValueError("O valor pago deve ser maior que zero")
        return self.validar_cpf()