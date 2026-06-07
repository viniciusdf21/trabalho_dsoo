from atendimento import Atendimento
from datetime import date, time


class ControladorAtendimento:
    def __init__(self):
        self.__atendimentos = []

    @property
    def atendimentos(self):
        return self.__atendimentos

    def cadastrar_atendimento(self, controlador_clinica, controlador_paciente, controlador_profissional, controlador_tipo_atendimento):
        try:
            clinica = controlador_clinica.escolher_clinica()
            if clinica is None:
                return
            paciente = controlador_paciente.escolher_paciente()
            if paciente is None:
                return
            profissional = controlador_profissional.escolher_profissional()
            if profissional is None:
                return
            tipo_atendimento = controlador_tipo_atendimento.escolher_tipo_atendimento()
            if tipo_atendimento is None:
                return

            data_atendimento = date(
                int(input("Ano do atendimento: ")),
                int(input("Mês do atendimento: ")),
                int(input("Dia do atendimento: "))
            )

            horario_inicio_texto = input("Horário de início (HH:MM): ")
            hora_inicio, minuto_inicio = horario_inicio_texto.split(":")
            horario_inicio = time(int(hora_inicio), int(minuto_inicio))

            horario_fim_texto = input("Horário de fim (HH:MM): ")
            hora_fim, minuto_fim = horario_fim_texto.split(":")
            horario_fim = time(int(hora_fim), int(minuto_fim))

            valor = float(input("Valor do atendimento: "))

            atendimento = Atendimento(clinica, paciente, profissional, data_atendimento, horario_inicio, horario_fim, tipo_atendimento, valor)

            atendimento.validar_atendimento()
            self.__atendimentos.append(atendimento)

            print("Atendimento cadastrado com sucesso.")

        except ValueError as erro:
            print(f"Erro ao cadastrar atendimento: {erro}")


    def listar_atendimentos(self):
        if not self.__atendimentos:
            print("Nenhum atendimento cadastrado.")
            return

        for atendimento in self.__atendimentos:
            print("\n")
            print(atendimento.exibir_dados())


    def escolher_atendimento(self):
        if not self.__atendimentos:
            print("Nenhum atendimento cadastrado.")
            return None

        print("\n=== ESCOLHER ATENDIMENTO ===")

        for i, atendimento in enumerate(self.__atendimentos):
            print(f"{i + 1} - {atendimento.paciente.nome} - {atendimento.data}")

        try:
            opcao = int(input("Escolha o atendimento: "))

            if opcao < 1 or opcao > len(self.__atendimentos):
                print("Atendimento inválido.")
                return None

            return self.__atendimentos[opcao - 1]

        except ValueError:
            print("Digite um número válido.")
            return None


    def alterar_atendimento(self, controlador_clinica, controlador_paciente, controlador_profissional, controlador_tipo_atendimento):
        atendimento = self.escolher_atendimento()

        if atendimento is None:
            return

        while True:
            print("\n=== ALTERAR ATENDIMENTO ===")
            print("1 - Alterar clínica")
            print("2 - Alterar paciente")
            print("3 - Alterar profissional")
            print("4 - Alterar tipo de atendimento")
            print("5 - Alterar data")
            print("6 - Alterar horário de início")
            print("7 - Alterar horário de fim")
            print("8 - Alterar valor")
            print("0 - Voltar")

            opcao = input("Opção: ")
            try:
                if opcao == "1":
                    nova_clinica = controlador_clinica.escolher_clinica()
                    if nova_clinica is not None:
                        atendimento.clinica = nova_clinica
                        atendimento.validar_atendimento()
                        print("Clínica alterada com sucesso.")
                elif opcao == "2":
                    novo_paciente = controlador_paciente.escolher_paciente()
                    if novo_paciente is not None:
                        atendimento.paciente = novo_paciente
                        atendimento.validar_atendimento()
                        print("Paciente alterado com sucesso.")
                elif opcao == "3":
                    novo_profissional = controlador_profissional.escolher_profissional()
                    if novo_profissional is not None:
                        atendimento.profissional = novo_profissional
                        atendimento.validar_atendimento()
                        print("Profissional alterado com sucesso.")
                elif opcao == "4":
                    novo_tipo_atendimento = controlador_tipo_atendimento.escolher_tipo_atendimento()
                    if novo_tipo_atendimento is not None:
                        atendimento.tipo_atendimento = novo_tipo_atendimento
                        atendimento.validar_atendimento()
                        print("Tipo de atendimento alterado com sucesso.")
                elif opcao == "5":
                    nova_data = date(
                        int(input("Novo ano do atendimento: ")),
                        int(input("Novo mês do atendimento: ")),
                        int(input("Novo dia do atendimento: "))
                    )
                    atendimento.data = nova_data
                    atendimento.validar_atendimento()
                    print("Data alterada com sucesso.")
                elif opcao == "6":
                    novo_horario_inicio_texto = input("Novo horário de início (HH:MM): ")
                    hora_inicio, minuto_inicio = novo_horario_inicio_texto.split(":")
                    novo_horario_inicio = time(int(hora_inicio), int(minuto_inicio))
                    atendimento.horario_inicio = novo_horario_inicio
                    atendimento.validar_atendimento()
                    print("Horário de início alterado com sucesso.")
                elif opcao == "7":
                    novo_horario_fim_texto = input("Novo horário de fim (HH:MM): ")
                    hora_fim, minuto_fim = novo_horario_fim_texto.split(":")
                    novo_horario_fim = time(int(hora_fim), int(minuto_fim))
                    atendimento.horario_fim = novo_horario_fim
                    atendimento.validar_atendimento()
                    print("Horário de fim alterado com sucesso.")
                elif opcao == "8":
                    novo_valor = float(input("Novo valor do atendimento: "))
                    atendimento.valor = novo_valor
                    atendimento.validar_atendimento()
                    print("Valor alterado com sucesso.")
                elif opcao == "0":
                    break
                else:
                    print("Opção inválida.")

            except ValueError as erro:
                print(f"Erro ao alterar atendimento: {erro}")


    def excluir_atendimento(self):
        atendimento = self.escolher_atendimento()

        if atendimento is None:
            return

        confirmacao = input("Tem certeza que deseja excluir este atendimento? (s/n): ")

        if confirmacao.lower() == "s":
            self.__atendimentos.remove(atendimento)
            print("Atendimento excluído com sucesso.")
        else:
            print("Exclusão cancelada.")


    def abrir_menu(self, controlador_clinica, controlador_paciente, controlador_profissional, controlador_tipo_atendimento):
        while True:
            print("\n=== ATENDIMENTOS ===")
            print("1 - Registrar")
            print("2 - Listar")
            print("3 - Alterar")
            print("4 - Excluir")
            print("0 - Voltar")

            opcao = input("Opção: ")
            if opcao == "1":
                self.cadastrar_atendimento(controlador_clinica, controlador_paciente, controlador_profissional, controlador_tipo_atendimento)
            elif opcao == "2":
                self.listar_atendimentos()
            elif opcao == "3":
                self.alterar_atendimento(controlador_clinica, controlador_paciente, controlador_profissional, controlador_tipo_atendimento)
            elif opcao == "4":
                self.excluir_atendimento()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")