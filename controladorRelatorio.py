class ControladorRelatorio:
    def abrir_menu(self, controlador_atendimento):
        while True:
            print("\n=== RELATÓRIOS ===")
            print("1 - Clínicas com maior número de atendimentos")
            print("2 - Atendimentos mais caro e mais barato")
            print("3 - Procedimentos mais realizados")
            print("4 - Procedimentos mais caro e mais barato")
            print("0 - Voltar")

            opcao = input("Opção: ")

            if opcao == "1":
                self.relatorio_clinicas_mais_atendimentos(controlador_atendimento)

            elif opcao == "2":
                self.relatorio_atendimentos_caros_baratos(controlador_atendimento)

            elif opcao == "3":
                self.relatorio_procedimentos_mais_realizados(controlador_atendimento)

            elif opcao == "4":
                self.relatorio_procedimentos_caros_baratos(controlador_atendimento)

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")

    def relatorio_clinicas_mais_atendimentos(self, controlador_atendimento):
        atendimentos = controlador_atendimento.atendimentos

        if not atendimentos:
            print("Nenhum atendimento cadastrado.")
            return

        contagem_clinicas = {}

        for atendimento in atendimentos:
            nome_clinica = atendimento.clinica.nome

            if nome_clinica in contagem_clinicas:
                contagem_clinicas[nome_clinica] += 1
            else:
                contagem_clinicas[nome_clinica] = 1

        maior_quantidade = max(contagem_clinicas.values())

        print("\n=== CLÍNICAS COM MAIOR NÚMERO DE ATENDIMENTOS ===")

        for nome_clinica, quantidade in contagem_clinicas.items():
            if quantidade == maior_quantidade:
                print(f"{nome_clinica} - {quantidade} atendimento(s)")

    def relatorio_atendimentos_caros_baratos(self, controlador_atendimento):
        atendimentos = controlador_atendimento.atendimentos

        if not atendimentos:
            print("Nenhum atendimento cadastrado.")
            return

        atendimento_mais_caro = atendimentos[0]
        atendimento_mais_barato = atendimentos[0]

        for atendimento in atendimentos:
            if atendimento.calcular_valor_total() > atendimento_mais_caro.calcular_valor_total():
                atendimento_mais_caro = atendimento

            if atendimento.calcular_valor_total() < atendimento_mais_barato.calcular_valor_total():
                atendimento_mais_barato = atendimento

        print("\n=== ATENDIMENTO MAIS CARO ===")
        print(atendimento_mais_caro.exibir_dados())

        print("\n=== ATENDIMENTO MAIS BARATO ===")
        print(atendimento_mais_barato.exibir_dados())

    def relatorio_procedimentos_mais_realizados(self, controlador_atendimento):
        atendimentos = controlador_atendimento.atendimentos

        if not atendimentos:
            print("Nenhum atendimento cadastrado.")
            return

        contagem_procedimentos = {}

        for atendimento in atendimentos:
            for procedimento in atendimento.lista_procedimentos:
                nome = procedimento.nome

                if nome in contagem_procedimentos:
                    contagem_procedimentos[nome] += 1
                else:
                    contagem_procedimentos[nome] = 1

        if not contagem_procedimentos:
            print("Nenhum procedimento registrado.")
            return

        maior_quantidade = max(contagem_procedimentos.values())

        print("\n=== PROCEDIMENTOS MAIS REALIZADOS ===")

        for nome, quantidade in contagem_procedimentos.items():
            if quantidade == maior_quantidade:
                print(f"{nome} - realizado {quantidade} vez(es)")

    def relatorio_procedimentos_caros_baratos(self, controlador_atendimento):
        atendimentos = controlador_atendimento.atendimentos

        if not atendimentos:
            print("Nenhum atendimento cadastrado.")
            return

        procedimentos = []

        for atendimento in atendimentos:
            for procedimento in atendimento.lista_procedimentos:
                procedimentos.append(procedimento)

        if not procedimentos:
            print("Nenhum procedimento registrado.")
            return

        procedimento_mais_caro = procedimentos[0]
        procedimento_mais_barato = procedimentos[0]

        for procedimento in procedimentos:
            if procedimento.custo > procedimento_mais_caro.custo:
                procedimento_mais_caro = procedimento

            if procedimento.custo < procedimento_mais_barato.custo:
                procedimento_mais_barato = procedimento

        print("\n=== PROCEDIMENTO MAIS CARO ===")
        print(procedimento_mais_caro.exibir_dados())

        print("\n=== PROCEDIMENTO MAIS BARATO ===")
        print(procedimento_mais_barato.exibir_dados())