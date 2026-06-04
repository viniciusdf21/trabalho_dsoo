from pagamento import Pagamento


class ControladorPagamento:
    def registrar_pagamento(self, pagamento: Pagamento):
        try:
            pagamento.registrar_pagamento()
            pagamento.atendimento.adicionar_pagamento(pagamento)

            return pagamento

        except ValueError as erro:
            print(f"Erro ao registrar pagamento: {erro}")
            return None


