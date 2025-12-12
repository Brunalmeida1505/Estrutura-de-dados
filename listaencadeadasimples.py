class Nodo:
    def __init__ (self, dado=0, proximo_nodo=None):
        self.conteudo = dado
        self.proximo = proximo_nodo
    def __repr__ (self):
        return '%s -> %s' % (self.conteudo, self.proximo)
class ListaEncadeada:
    def __init__(self):
        self.inicio = None
    def __repr__(self):
        return "[" + str(self.inicio) + "]"
    def ListaVazia(Lista):
        if Lista.inicio == None:
            return True
        else:
            return False
def TamanhoLista(self):
    atual = self.inicio
    tamanho = 0
    if self.inicio == None:
        return 0
    if atual.conteudo != None and atual.proximo == None:
        tamanho =  1
    while atual.proximo != None:
        tamanho = tamanho+1
        atual = atual.proximo
def Adiciona_Inicio(self, Nd):
    atual = self.inicio
    Nd.proximo = atual
    self.inicio = Nd
def Adiciona_Fim(self, item):
    if self.inicio:
        aux = self.inicio
        while (aux.proximo):
            aux = aux.proximo
        aux.proximo = item
    else:
        self.inicio = item
def Adiciona_Pos(self, item, pos):
    atual = self.inicio
    pos_atual = 0
    while atual.proximo != None:
        if pos_atual == (pos-1):
            pointer = atual
            item.proximo = pointer.proximo
            pointer.proximo = item
        else:
            atual = atual.proximo
        pos_atual = pos_atual + 1
def Remove_Pos(self,pos):
    atual = self.inicio
    pos_atual = 0
    if pos_atual == pos:
        self.inicio = atual.proximo
    else:
        while atual.proximo != None:
            if pos_atual == (pos-1):
                next = atual.proximo
                atual.proximo = next.proximo
            else:
                atual = atual.proximo
            pos_atual = pos_atual + 1
def Remove_Inicio(self):
    atual = self.inicio
    self.inicio = atual.proximo
def Remove_Ultimo(self):
    atual = self.inicio
    while atual.proximo != None:
        proximo = atual.proximo
        if proximo.proximo == None:
            atual.proximo = None
        else:
            atual = atual.proximo            
def Ocorrencia(self, dado):
    atual =self.inicio
    total_ocorrencia = 0
    while atual != None:
        if atual.conteudo == dado:
            total_ocorrencia = total_ocorrencia + 1
            atual = atual.proximo
        else:
            atual = atual.proximo
    return total_ocorrencia

Nd = Nodo("A")
Adiciona_Fim(lista,Nd)
print("lista: ",lista)

Nd2 = Nodo("B")
Adiciona_Fim(lista,Nd2)
print("lista: ",lista)

Nd3 = Nodo("A")
Adiciona_Fim(lista,Nd3)
print("lista: ",lista)


print("Ocorrência da letra A: ", Ocorrencia(lista, "A"))