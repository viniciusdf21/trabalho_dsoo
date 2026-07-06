from DAO.dao import DAO
from procedimento import Procedimento


class ProcedimentoDAO(DAO):

    def __init__(self):
        super().__init__("procedimentos.pkl")

    def gerar_chave(self, procedimento: Procedimento):
        return (
            f"{procedimento.nome}_"
            f"{procedimento.profissional.cpf}"
        )

    def add(self, procedimento: Procedimento):
        if isinstance(procedimento, Procedimento):
            chave = self.gerar_chave(procedimento)
            super().add(chave, procedimento)

    def update(self, procedimento: Procedimento):
        if isinstance(procedimento, Procedimento):
            chave = self.gerar_chave(procedimento)
            super().update(chave, procedimento)

    def remove(self, procedimento: Procedimento):
        if isinstance(procedimento, Procedimento):
            chave = self.gerar_chave(procedimento)
            super().remove(chave)
