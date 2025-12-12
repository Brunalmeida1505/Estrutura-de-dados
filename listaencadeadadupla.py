class Elemento(object):
    def __init__(self, info):
        self.info = info
        self.ant = None
        self.prox = None
class ListaDupla(object):
    def __init__(self):
        self.inicio = None
        self.fim = None
        print("Lista criada")
    def lista_vazia(self):
        return self.inicio is None
    def adicionar_fim(self, info : int) -> None:
        novo_e = Elemento(info)
        if self.lista_vazia():
            self.inicio = novo_e
            self.fim = novo_e
        else:
            novo_e.ant = self.fim
            novo_e.prox = None
            self.fim.prox = novo_e
            self.fim = novo_e
        print("Elemento adicionado: {0}. \n".format(novo_e.info))
    def remover(self,info):
        e_atual = self.inicio
        while e_atual is not None:
            if e_atual.info == info:
                if e_atual.ant is None:
                    self.inicio = e_atual.prox
                    e_atual.prox.ant = None
                else:
                    e_atual.ant.prox = e_atual.prox
                    e_atual.prox.ant = e_atual.ant
                print("\nElemento {0} removido".format(e_atual.info))
                break
            e_atual = e_atual.prox
    def imprimir_crescente(self):
        e_atual = self.inicio
        elemento = ""
        while e_atual is not None:
            if e_atual.ant is None:
                elemento += "None "
            elemento += "<-> | " + str(e_atual.info) + " | "
            if e_atual.prox is None:
                elemento += "<-> None"
            e_atual = e_atual.prox
        print("Em ordem Crescente: \n")
        print(elemento)
        print("="*60)
    def imprimir_decrescente(self):
        e_atual = self.fim
        elemento = ""
        while e_atual is not None:
            if e_atual.prox is None:
                elemento += "None "
            elemento += "<-> | " + str(e_atual.info) + " | "
            if e_atual.ant is None:
                elemento += "<-> None"
            e_atual = e_atual.ant
        print("Em ordem Decrescente: \n")
        print(elemento)
        print("="*60)
lista = ListaDupla()
lista.adicionar_fim(3)
lista.adicionar_fim(45)
lista.adicionar_fim(2)
lista.adicionar_fim(1)
lista.adicionar_fim(19)

lista.imprimir_crescente()