from atendimento import Atendimento
from datetime import date, time


class ControladorAtendimento:
    def __init__(self):
        self.__atendimentos = []

    @property
    def atendimentos(self):
        return self.__atendimentos

    def cadastrar_atendimento(self, clinica, paciente, profissional, tipo_atendimento):
        try:
            ano = int(input("Ano do atendimento: "))
            mes = int(input("Mês do atendimento: "))
            dia = int(input("Dia do atendimento: "))
            data_atendimento = date(ano, mes, dia)

            hora_inicio = int(input("Hora de início: "))
            minuto_inicio = int(input("Minuto de início: "))
            horario_inicio = time(hora_inicio, minuto_inicio)

            hora_fim = int(input("Hora de fim: "))
            minuto_fim = int(input("Minuto de fim: "))
            horario_fim = time(hora_fim, minuto_fim)

            valor = float(input("Valor do atendimento: "))

            atendimento = Atendimento(
                clinica,
                paciente,
                profissional,
                data_atendimento,
                horario_inicio,
                horario_fim,
                tipo_atendimento,
                valor
            )
            
            atendimento.validar_atendimento()
            self.__atendimentos.append(atendimento)
            print("Atendimento cadastrado com sucesso.")
            return atendimento
        except ValueError as erro:
            print(f"Erro ao cadastrar atendimento: {erro}")
            return None

    def listar_atendimentos(self):
        if not self.__atendimentos:
            print("Nenhum atendimento cadastrado.")
            return
        for atendimento in self.__atendimentos:
            print("\n")
            print(atendimento.exibir_dados())

    def remover_atendimento(self, atendimento):
        try:
            if atendimento not in self.__atendimentos:
                raise ValueError("Atendimento não encontrado.")
            self.__atendimentos.remove(atendimento)
            print("Atendimento removido com sucesso.")
            return True
        except ValueError as erro:
            print(f"Erro ao remover atendimento: {erro}")
            return False