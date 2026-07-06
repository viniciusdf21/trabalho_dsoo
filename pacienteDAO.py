from dao import DAO
from paciente import Paciente


class PacienteDAO(DAO):

    def __init__(self):
        super().__init__("pacientes.pkl")

    def add(self, paciente: Paciente):
        if isinstance(paciente, Paciente):
            super().add(paciente.cpf, paciente)

    def update(self, paciente: Paciente):
        if isinstance(paciente, Paciente):
            super().update(paciente.cpf, paciente)

    def remove(self, paciente: Paciente):
        if isinstance(paciente, Paciente):
            super().remove(paciente.cpf)
