from datetime import datetime, time

class Clinica():
    def __init__(self, nome, loc, descricao, horario_abertura, horario_fechamento):
        self.__nome = nome
        self.__loc = loc
        self.__descricao = descricao
        self.__horario_abertura = horario_abertura
        self.__horario_fechamento = horario_fechamento
        self.__atendimentos = []

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
        
    @property
    def loc(self):
        return self.__loc
    
    @loc.setter
    def loc(self, nova_loc):
        self.__loc = nova_loc
        
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, nova_desc):
        self.__descricao = nova_desc
        
    @property
    def horario_abertura(self):
        return self.horario_abertura
    
    @horario_abertura.setter
    def horario_abertura(self, novo_ha):
        if not isinstance(novo_ha, time):
            raise ValueError("O horário deve ser do tipo time.")
        self.horario_abertura = novo_ha
        
    @property
    def horario_fechamento(self):
        return self.horario_fechamento
    
    @horario_fechamento.setter
    def horario_fechamento(self, novo_hf):
        if not isinstance(novo_hf, time):
            raise ValueError("O horário deve ser do tipo time")
        self.horario_fechamento = novo_hf
        
    def verificar_funcionamento(self):
        hora_atual = datetime.now().time()
        return self.horario_abertura <= hora_atual <= self.horario_fechamento
        
    def exibir_dados(self):
        return (
            f"Nome: {self.nome}\n"
            f"Localização: {self.loc}\n"
            f"Descrição: {self.descricao}\n"
            f"Horário de abertura: {self.horario_abertura}\n"
            f"Horário de fechamento: {self.horario_fechamento}"
        )
