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
    def __init__ (self):
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



    def removerPrimeiro(self): #remove o primeiro elemento da lista
        if self.__inicio != None: #se a lista não estiver vazia, altera o início da lista para o próximo elemento
            self.__inicio = self.__inicio.pegaProx()

        if self.__inicio == None: #se a lista ficar vazia após a remoção, o último elemento também deve ser None
            self.__fim = None



    def inserirAntesDe(self, posicao, novo): #insere um elemento antes de outro elemento da lista
        atual = self.__inicio

        if atual == None:
            raise Exception("Lista vazia")

        if atual == posicao:
            self.inserirComoPrimeiro(novo)
            return

        while posicao != atual.pegaProx() and atual.pegaProx() != None:
            atual = atual.pegaProx()

        if atual.pegaProx() == None:
            raise Exception("Posição inválida")

        novo.alteraProx(atual.pegaProx())
        atual.alteraProx(novo)



    def inserirNaPosicao(self, posicao, novo): #insere um elemento em uma posição específica da lista
        if posicao == 0:
            self.inserirComoPrimeiro(novo)
            return

        atual = self.__inicio
        contador = 0

        while contador < posicao - 1 and atual != None:
            atual = atual.pegaProx()
            contador += 1

        if atual == None:
            raise Exception("Posição inválida")

        novo.alteraProx(atual.pegaProx())
        atual.alteraProx(novo)

        if novo.pegaProx() == None:
            self.__fim = novo



    def acessaUltimo(self): #retorna o último elemento da lista
        return self.__fim


    def acessaDaPosicao(self, posicao): #retorna o elemento de uma posição específica da lista
        if posicao == 0:
            return self.__inicio

        atual = self.__inicio
        contador = 0

        while contador < posicao - 1 and atual != None:
            atual = atual.pegaProx()
            contador += 1

        if atual == None:
            raise Exception("Posição inválida")

        return atual.pegaProx()


    def busca(self, referencia): #verifica se um elemento está presente na lista, se tiver retorna True, se não estiver retorna False
        atual = self.__inicio

        while atual != None:
            if atual == referencia:
                return True
            atual = atual.pegaProx()
        return False


#testes 

#criando a lista
lista = Lista()

#criando elementos
elemento1 = Elemento(1)
elemento2 = Elemento(2)
elemento3 = Elemento(3)
elemento4 = Elemento(4)
elemento5 = Elemento(5)

#inserir como primeiro
lista.inserirComoPrimeiro(elemento1)
print("Primeiro:", lista.acessaDaPosicao(0).pegaValor()) #deve imprimir 1

#inserir outro como primeiro
lista.inserirComoPrimeiro(elemento2)
print("Primeiro atual:", lista.acessaDaPosicao(0).pegaValor()) #deve imprimir 2

#inserir como último
lista.inserirComoUltimo(elemento3)
print("Último:", lista.acessaUltimo().pegaValor()) #deve imprimir 3

#inserir antes de um elemento
lista.inserirAntesDe(elemento1, elemento4)
print("Elemento 4 inserido antes do elemento 1")
print("Elemento na posição 0:", lista.acessaDaPosicao(0).pegaValor()) #deve imprimir 2
print("Elemento na posição 1:", lista.acessaDaPosicao(1).pegaValor()) #deve imprimir 4
print("Elemento na posição 2:", lista.acessaDaPosicao(2).pegaValor()) #deve imprimir 1
print("Elemento na posição 3:", lista.acessaDaPosicao(3).pegaValor()) #deve imprimir 3

#inserir na posição
lista.inserirNaPosicao(2, elemento5)
print("Elemento 5 inserido na posição 2")
print("Elemento na posição 0:", lista.acessaDaPosicao(0).pegaValor()) #deve imprimir 2
print("Elemento na posição 1:", lista.acessaDaPosicao(1).pegaValor()) #deve imprimir 4
print("Elemento na posição 2:", lista.acessaDaPosicao(2).pegaValor()) #deve imprimir 5
print("Elemento na posição 3:", lista.acessaDaPosicao(3).pegaValor()) #deve imprimir 1
print("Elemento na posição 4:", lista.acessaDaPosicao(4).pegaValor()) #deve imprimir 3

#verica o ultimo elemento
print("Último elemento:", lista.acessaUltimo().pegaValor()) #deve imprimir 3

#testando a busca
print("Busca elemento 1:", lista.busca(elemento1)) #deve imprimir True
print("Busca elemento 6:", lista.busca(Elemento(6))) #deve imprimir False

#testar remover o primeiro elemento
lista.removerPrimeiro()
print("Primeiro elemento após remover o primeiro:", lista.acessaDaPosicao(0).pegaValor()) #deve imprimir 4

#testar ultimo apos inserir na ultima posicao
elemtento6 = Elemento(6)
lista.inserirNaPosicao(4, elemtento6)
print("Último elemento após inserir na última posição:", lista.acessaUltimo().pegaValor()) #deve imprimir 6
