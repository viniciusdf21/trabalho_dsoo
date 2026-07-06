from dao import DAO
from clinica import Clinica


class ClinicaDAO(DAO):

    def __init__(self):
        super().__init__("clinicas.pkl")

    def add(self, clinica: Clinica):
        if isinstance(clinica, Clinica):
            super().add(clinica.nome, clinica)

    def update(self, clinica: Clinica):
        if isinstance(clinica, Clinica):
            super().update(clinica.nome, clinica)

    def remove(self, clinica: Clinica):
        if isinstance(clinica, Clinica):
            super().remove(clinica.nome)
