from pessoa import Pessoa
from datetime import date


class Paciente(Pessoa):
    def __init__(self, nome, cpf, telefone, data_nascimento):
        super().__init__(nome, cpf, telefone)
        self.data_nascimento = data_nascimento

    @property
    def data_nascimento(self):
        return self.data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, nova_data):
        if not isinstance(nova_data, date):
            raise ValueError("A data de nascimento deve ser do tipo date.")
        self.data_nascimento = nova_data

    def verificar_idade(self):
        hoje = date.today()
        idade = hoje.year - self.data_nascimento.year
        
        if (hoje.month, hoje.day) < (
            self.data_nascimento.month,
            self.data_nascimento.day
        ):
            idade -= 1
            
        return idade

    def exibir_dados(self):
        return (
            f"Nome: {self.__nome}\n"
            f"CPF: {self.__cpf}\n"
            f"Celular: {self.__celular}\n"
            f"Data de nascimento: {self.data_nascimento}\n"
            f"Idade: {self.verificar_idade()} anos"
        )
        
