#Trabalinho lista encadeada simples
#Alunos: Nicole Motta Rodrigues, Vinicius Dalmarco Fronza


class Elemento:
    def __init__ (self, dado):
        self.__valor = dado
        self.__prox = None

    def pegaValor(self):
        return self.__valor

    def pegaProx(self):
        return self.__prox

    def alteraProx(self, novo):
        self.__prox = novo


class Lista:
    def __init__(self):
        self.__inicio = None
        self.__fim = None

    def inserirComoPrimeiro(self, novo): #insere um elemento no início da lista
        novo.alteraProx(self.__inicio)
        self.__inicio = novo

        if self.__fim == None: #se a lista estava vazia, o novo elemento também é o último
            self.__fim = novo

    def inserirComoUltimo(self, novo): #insere um elemento no final da lista
        if self.__inicio == None: #se a lista estiver vazia, o novo elemento será o primeiro e o último
            self.__inicio = novo
            self.__fim = novo
        else:
            self.__fim.alteraProx(novo) #altera o próximo do último elemento para o novo elemento
            self.__fim = novo

    def inserirNaPosicao(self, posicao, novo): #insere um elemento em uma posição específica da lista
        if posicao == 0: #se a posição for 0, o novo elemento será inserido como primeiro
            self.inserirComoPrimeiro(novo)
            return

        atual = self.__inicio
        contador = 0

        while contador < posicao - 1 and atual != None: #percorre a lista até chegar na posição desejada ou no final da lista
            atual = atual.pegaProx()
            contador += 1

        if atual == None: #se a posição for inválida (maior que o tamanho da lista), lança uma exceção
            raise Exception("Posição inválida")

        novo.alteraProx(atual.pegaProx())
        atual.alteraProx(novo)

        if novo.pegaProx() == None: #se o novo elemento for inserido na última posição, atualiza o último elemento da lista
            self.__fim = novo

    def inserirAntesDe(self, referencia, novo): #insere um elemento antes de outro elemento da lista
        atual = self.__inicio

        if atual == None: #se a lista estiver vazia, não é possível inserir antes de um elemento
            raise Exception("Lista vazia")

        if atual == referencia: #se a referência for o primeiro elemento, o novo elemento será inserido como primeiro
            self.inserirComoPrimeiro(novo)
            return

        while referencia != atual.pegaProx() and atual.pegaProx() != None: #percorre a lista até encontrar a referência ou chegar ao final da lista
            atual = atual.pegaProx()

        if atual.pegaProx() == None: #se a referência não for encontrada na lista, lança uma exceção
            raise Exception("Referencia inválida")

        novo.alteraProx(atual.pegaProx())
        atual.alteraProx(novo)

    def inserirDepoisDe(self, referencia, novo): #insere um novo elemento depois do elemento informado em "referencia"
        atual = self.__inicio  
        while atual != None and atual != referencia: # while para percorrer a lista ate encontrar a referencia
            atual = atual.pegaProx()

        if atual == None: #caso while finaliza sem encontrar a referencia, mensagem de "nao encontrada" aparece
            raise Exception("Referência não encontrada")

        novo.alteraProx(atual.pegaProx()) # o novo aponta para quem vinha depois da referencia
        atual.alteraProx(novo)  # a referencia passa a apontar para o novo elemento
        if atual == self.__fim:  # se a referencia era o ultimo elemento, atualiza o fim da lista
            self.__fim = novo

    def removerPrimeiro(self): #remove o primeiro elemento da lista
        if self.__inicio != None: #se a lista não estiver vazia, altera o início da lista para o próximo elemento
            self.__inicio = self.__inicio.pegaProx()

        if self.__inicio == None: #se a lista ficar vazia após a remoção, o último elemento também deve ser None
            self.__fim = None

    def removerUltimo(self): #remove o ultimo elemento da lista
        if self.__inicio == None: #avisa caso a lista esteja vazia
            raise Exception("Lista vazia")
        if self.__inicio == self.__fim: # se existe apenas um elemento, a lista fica vazia
            self.__inicio = None
            self.__fim = None
            return

        atual = self.__inicio  # comeca a busca pelo primeiro elemento
        while atual.pegaProx() != self.__fim: # while para percorrer ate encontrar o elemento anterior ao ultimo
            atual = atual.pegaProx()

        atual.alteraProx(None)  # o penultimo deixa de apontar para o ultimo
        self.__fim = atual      # atualiza o fim da lista

    def removerDaPosicao(self, posicao): #remove o elemento localizado na posicao informada
        if self.__inicio == None: #verifica se a lista ta vazia
            raise Exception("Lista vazia")

        if posicao < 0: #se a posicao for menor que zero, fica invalida
            raise Exception("Posição inválida")

        if posicao == 0: # se a posicao for 0, remove o primeiro elemento
            self.removerPrimeiro()
            return

        anterior = self.__inicio
        contador = 0
        while contador < posicao - 1 and anterior.pegaProx() != None: # while para percorrer ate chegar ao elemento que ta antes da posicao desejada
            anterior = anterior.pegaProx()
            contador += 1

        if anterior.pegaProx() == None: # se nao existe elemento na posicao informada
            raise Exception("Posição inválida")

        remover = anterior.pegaProx()  # guarda o elemento que sera removido
        anterior.alteraProx(remover.pegaProx()) # faz o anterior apontar para o elemento seguinte ao removido
        if remover == self.__fim: # se o elemento removido era o ultimo, atualiza o fim
            self.__fim = anterior

    def remover(self, referencia): #remove da lista o elemento informado como referência
        if self.__inicio == None:
            raise Exception("Lista vazia")
        if self.__inicio == referencia: # se a referencia for o primeiro elemento
            self.removerPrimeiro()
            return

        anterior = self.__inicio
        atual = self.__inicio.pegaProx()
        while atual != None and atual != referencia: # while para percorrer a lista ate encontrar a referencia
            anterior = atual
            atual = atual.pegaProx()

        if atual == None: # se chegou ao fim sem encontrar a referencia
            raise Exception("Referência não encontrada")

        anterior.alteraProx(atual.pegaProx()) # faz o anterior apontar para o elemento seguinte ao removido
        if atual == self.__fim: # se o elemento removido era o ultimo, atualiza o fim
            self.__fim = anterior

    def acessaPrimeiro(self): #retorna o primeiro elemento da lista
        if self.__inicio == None:
            raise Exception("Lista vazia")
        return self.__inicio  # retorna o primeiro elemento

    def acessaUltimo(self): #retorna o último elemento da lista
        return self.__fim

    def acessaDaPosicao(self, posicao): #retorna o elemento de uma posição específica da lista
        if posicao == 0: #se a posição for 0, retorna o primeiro elemento da lista
            return self.__inicio

        atual = self.__inicio
        contador = 0

        while contador < posicao - 1 and atual != None: #percorre a lista até chegar na posição desejada ou no final da lista
            atual = atual.pegaProx()
            contador += 1

        if atual == None: #se a posição for inválida (maior que o tamanho da lista), lança uma exceção
            raise Exception("Posição inválida")

        return atual.pegaProx() #retorna o elemento da posição desejada (o próximo do elemento atual)

    def busca(self, referencia): #verifica se um elemento está presente na lista, se tiver retorna True, se não estiver retorna False
        atual = self.__inicio

        while atual != None: #percorre a lista até encontrar o elemento ou chegar ao final da lista
            if atual == referencia: #se o elemento atual for igual à referência, retorna True
                return True
            atual = atual.pegaProx()
        return False


# TESTES
lista = Lista()

elemento1 = Elemento(1)
elemento2 = Elemento(2)
elemento3 = Elemento(3)
elemento4 = Elemento(4)
elemento5 = Elemento(5)

# INSERÇÕES
lista.inserirComoPrimeiro(elemento1)
lista.inserirComoUltimo(elemento3)
lista.inserirNaPosicao(1, elemento2)
lista.inserirAntesDe(elemento2, elemento4)
lista.inserirDepoisDe(elemento2, elemento5)

print("Lista após inserções:")
print(lista.acessaDaPosicao(0).pegaValor())
print(lista.acessaDaPosicao(1).pegaValor())
print(lista.acessaDaPosicao(2).pegaValor())
print(lista.acessaDaPosicao(3).pegaValor())
print(lista.acessaDaPosicao(4).pegaValor())

# ACESSOS
print("Primeiro:", lista.acessaPrimeiro().pegaValor())
print("Último:", lista.acessaUltimo().pegaValor())
print("Elemento na posição 2:", lista.acessaDaPosicao(2).pegaValor())
print("Busca elemento 5:", lista.busca(elemento5))

# REMOÇÕES
lista.removerPrimeiro()
lista.removerUltimo()
lista.removerDaPosicao(1)
lista.remover(elemento5)

print("Lista após remoções:")
print(lista.acessaDaPosicao(0).pegaValor())
