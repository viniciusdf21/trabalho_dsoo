from DAO.dao import DAO
from profissional import Profissional


class ProfissionalDAO(DAO):

    def __init__(self):
        super().__init__("profissionais.pkl")

    def add(self, profissional: Profissional):
        if isinstance(profissional, Profissional):
            super().add(profissional.cpf, profissional)

    def update(self, profissional: Profissional):
        if isinstance(profissional, Profissional):
            super().update(profissional.cpf, profissional)

    def remove(self, profissional: Profissional):
        if isinstance(profissional, Profissional):
            super().remove(profissional.cpf)
