class TelaPaciente:

    def pegar_dados_paciente(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        celular = input("Celular: ")

        return nome, cpf, celular

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
