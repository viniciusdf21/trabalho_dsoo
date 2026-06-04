from procedimento import Procedimento


class ControladorProcedimento:
    def registrar_procedimento(self, atendimento, procedimento: Procedimento):
        atendimento.adicionar_procedimento(procedimento)

        return procedimento