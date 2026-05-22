class Atendimento():
    def __init__(self, clinica, paciente, profissional, data, horario_inicio, horario_fim , tipo_atendimento, valor):
        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.__data = data
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__tipo_atendimento = tipo_atendimento
        self.__valor = valor
        self.__lista_procendimentos = []
        self.__lista_pagamentos = []
