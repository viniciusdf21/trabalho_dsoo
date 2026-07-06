from DAO.dao import DAO
from tipoAtendimento import TipoAtendimento


class TipoAtendimentoDAO(DAO):

    def __init__(self):
        super().__init__("tipos_atendimento.pkl")

    def add(self, tipo: TipoAtendimento):
        if isinstance(tipo, TipoAtendimento):
            super().add(tipo.nome, tipo)

    def update(self, tipo: TipoAtendimento):
        if isinstance(tipo, TipoAtendimento):
            super().update(tipo.nome, tipo)

    def remove(self, tipo: TipoAtendimento):
        if isinstance(tipo, TipoAtendimento):
            super().remove(tipo.nome)
