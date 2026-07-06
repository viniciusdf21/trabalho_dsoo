from DAO.dao import DAO
from pagamento import Pagamento


class PagamentoDAO(DAO):

    def __init__(self):
        super().__init__("pagamentos.pkl")

    def gerar_chave(self, pagamento: Pagamento):
        return (
            f"{pagamento.atendimento.paciente.cpf}_"
            f"{pagamento.atendimento.data}_"
            f"{pagamento.atendimento.horario_inicio.strftime('%H%M')}_"
            f"{pagamento.data_pagamento}_"
            f"{pagamento.valor_pago}_"
            f"{pagamento.__class__.__name__}"
        )

    def add(self, pagamento: Pagamento):
        if isinstance(pagamento, Pagamento):
            chave = self.gerar_chave(pagamento)
            super().add(chave, pagamento)

    def update(self, pagamento: Pagamento):
        if isinstance(pagamento, Pagamento):
            chave = self.gerar_chave(pagamento)
            super().update(chave, pagamento)

    def remove(self, pagamento: Pagamento):
        if isinstance(pagamento, Pagamento):
            chave = self.gerar_chave(pagamento)
            super().remove(chave)
