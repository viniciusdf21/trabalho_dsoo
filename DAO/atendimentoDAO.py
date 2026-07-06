from DAO.dao import DAO
from atendimento import Atendimento


class AtendimentoDAO(DAO):

    def __init__(self):
        super().__init__("atendimentos.pkl")

    def gerar_chave(self, atendimento: Atendimento):
        return (
            f"{atendimento.paciente.cpf}_"
            f"{atendimento.data}_"
            f"{atendimento.horario_inicio.strftime('%H%M')}"
        )

    def add(self, atendimento: Atendimento):
        if isinstance(atendimento, Atendimento):
            chave = self.gerar_chave(atendimento)
            super().add(chave, atendimento)

    def update(self, atendimento: Atendimento):
        if isinstance(atendimento, Atendimento):
            chave = self.gerar_chave(atendimento)
            super().update(chave, atendimento)

    def remove(self, atendimento: Atendimento):
        if isinstance(atendimento, Atendimento):
            chave = self.gerar_chave(atendimento)
            super().remove(chave)
