class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def setNome(self, nome):
        self.nome = nome
    
    def setIdade(self, idade):
        self.idade = idade
    
    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade

class Conta:
    def __init__(self, nome= "", numero="", saldo = 0):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo
    
    def alterarNomeConta(self):
        self.nome = input('Nome: ')
        self.menu()
    
    def deposito(self):
        novaQuantia = float(input('Depósito\nNova quantia: '))
        self.saldo = self.saldo + novaQuantia
        self.menu()

    def saque(self):
        novoSaque = float(input('Saque\nValor do Saque: '))
        self.saldo = self.saldo - novoSaque
        self.menu()
    
    def saldo(self):
        print(self.saldo)
        self.menu()

class Banco:
    listaDeContas = []

    def iniciaConta(self):
        nome = input('Nome do titualar: ')
        numero = input('Número da conta: ')
        novaConta = Conta(nome, numero)
        self.listaDeContas.append(novaConta)
        self.menuBanco()

    def acessarConta(self):
        numero = input('Número da conta: \n')
        for conta in self.listaDeContas:
            if(numero == conta.numero):
                conta.menu()
    
    def exluirConta(self):
        numero = input("Número da conta: \n")
        for conta in self.listaDeContas:
            if(numero == conta.numero):
                print(conta.nome)

class Menu:
    def menuCliente():
        print('---MENU BANCO---' \
        '1 - ALTERAR NOME DA CONTA\n' \
        '2 - NOVO DEPOSITO\n' \
        '3 - NOVO SAQUE' \
        '4 - VISUALIZAR SAQUE')
c = Conta()
m = Menu()

print(m.menuCliente())
while True:
    escolha = m.menuCliente()
    if escolha == 1:
        c.alterarNomeConta()