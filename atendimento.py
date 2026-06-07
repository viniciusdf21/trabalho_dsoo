from datetime import date, time


class Atendimento:
    def __init__(self, clinica, paciente, profissional, data, horario_inicio, horario_fim, tipo_atendimento, valor):
        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.data = data
        self.horario_inicio = horario_inicio
        self.horario_fim = horario_fim
        self.__tipo_atendimento = tipo_atendimento
        self.valor = valor
        self.__lista_procedimentos = []
        self.__lista_pagamentos = []

    @property
    def clinica(self):
        return self.__clinica

    @clinica.setter
    def clinica(self, clinica):
        self.__clinica = clinica

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente):
        self.__paciente = paciente

    @property
    def profissional(self):
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional):
        self.__profissional = profissional

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, date):
            raise ValueError("A data do atendimento deve ser do tipo date.")
        self.__data = data

    @property
    def horario_inicio(self):
        return self.__horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, horario_inicio):
        if not isinstance(horario_inicio, time):
            raise ValueError("O horário de início deve ser do tipo time.")
        self.__horario_inicio = horario_inicio

    @property
    def horario_fim(self):
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, horario_fim):
        if not isinstance(horario_fim, time):
            raise ValueError("O horário de fim deve ser do tipo time.")
        self.__horario_fim = horario_fim

    @property
    def tipo_atendimento(self):
        return self.__tipo_atendimento

    @tipo_atendimento.setter
    def tipo_atendimento(self, tipo_atendimento):
        self.__tipo_atendimento = tipo_atendimento

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        if valor <= 0:
            raise ValueError("O valor do atendimento deve ser maior que zero.")
        self.__valor = valor

    @property
    def lista_procedimentos(self):
        return self.__lista_procedimentos

    @lista_procedimentos.setter
    def lista_procedimentos(self, lista_procedimentos):
        self.__lista_procedimentos = lista_procedimentos

    @property
    def lista_pagamentos(self):
        return self.__lista_pagamentos

    @lista_pagamentos.setter
    def lista_pagamentos(self, lista_pagamentos):
        self.__lista_pagamentos = lista_pagamentos

    def adicionar_procedimento(self, procedimento):
        if procedimento is None:
            raise ValueError("Procedimento inválido.")
        self.__lista_procedimentos.append(procedimento)

    def adicionar_pagamento(self, pagamento):
        if pagamento is None:
            raise ValueError("Pagamento inválido.")
        self.__lista_pagamentos.append(pagamento)

    def calcular_valor_total(self):
        total = self.__valor
        for procedimento in self.__lista_procedimentos:
            total += procedimento.custo
        return total

    def calcular_valor_restante(self):
        total_pago = 0
        for pagamento in self.__lista_pagamentos:
            total_pago += pagamento.valor_pago
        return self.calcular_valor_total() - total_pago

    def validar_horario(self):
        if self.__horario_inicio >= self.__horario_fim:
            raise ValueError("O horário de início deve ser menor que o horário de fim.")
        if self.__horario_inicio < self.__clinica.horario_abertura:
            raise ValueError("O atendimento não pode começar antes da abertura da clínica.")
        if self.__horario_fim > self.__clinica.horario_fechamento:
            raise ValueError("O atendimento não pode terminar depois do fechamento da clínica.")
        return True

    def validar_idade_paciente(self):
        if self.__paciente.verificar_idade() < 18:
            raise ValueError("O paciente deve ter pelo menos 18 anos.")
        return True

    def validar_atendimento(self):
        self.validar_horario()
        self.validar_idade_paciente()
        if self.__valor <= 0:
            raise ValueError("O valor do atendimento deve ser maior que zero.")
        return True

    def exibir_dados(self):
        return (
        f"Clínica: {self.__clinica.nome}\n"
        f"Paciente: {self.__paciente.nome}\n"
        f"Profissional: {self.__profissional.nome}\n"
        f"Data: {self.__data}\n"
        f"Horário de início: {self.__horario_inicio.strftime('%H:%M')}\n"
        f"Horário de fim: {self.__horario_fim.strftime('%H:%M')}\n"
        f"Tipo de atendimento: {self.__tipo_atendimento.nome}\n"
        f"Valor base: R$ {self.__valor:.2f}\n"
        f"Valor total: R$ {self.calcular_valor_total():.2f}\n"
        f"Valor restante: R$ {self.calcular_valor_restante():.2f}")
        