class Procedimento:
    def __init__(self, nome, descricao, custo, profissional):
        self.nome = nome
        self.descricao = descricao
        self.custo = custo
        self.profissional = profissional

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def custo(self):
        return self.__custo

    @custo.setter
    def custo(self, custo):
        if custo <= 0:
            raise ValueError("O custo do procedimento deve ser maior que zero.")
        self.__custo = custo

    @property
    def profissional(self):
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional):
        self.__profissional = profissional
    
    def exibir_dados(self):
        return (
            f"Nome do procedimento: {self.__nome}\n"
            f"Descrição: {self.__descricao}\n"
            f"Custo: R$ {self.__custo:.2f}\n"
            f"Profissional: {self.__profissional.nome}"
        )