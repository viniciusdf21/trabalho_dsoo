class TipoAtendimento():
    def __init__(self, nome, descricao, valor_base):
        self.__nome = nome
        self.__descricao = descricao
        self.__valor_base = valor_base

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
        
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, nova_d):
        self.__descricao = nova_d
        
    @property
    def valor_base(self):
        return self.__valor_base
    
    @valor_base.setter
    def valor_base(self, novo_valor_base):
        self.__valor_base = novo_valor_base
