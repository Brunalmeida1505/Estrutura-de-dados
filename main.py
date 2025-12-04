"""
Estratégia:
Usei a estrutura de dados pilhas . Para cada '(' ou '[' empilhei.
Para cada ')' ou ']' verifiquei o topo da pilha — se não corresponder,
a expressão é MALFORMADA. Ao final, se a pilha estiver vazia, a expressão e bem-formada.

Leitura:
Se uma linha contém o caractere 'X', considero
apenas a parte antes do primeiro 'X' como última expressão e então
encerro o programa atendendo a chave de parada.
"""

import sys

MAX_CARACTERE = 100

def bem_formada(expressao):
    pilha = []
    pares = {')': '(', ']': '['}
    for chave in expressao:
        if chave in '([':
            pilha.append(chave)
        elif chave in ')]':
            if not pilha or pilha[-1] != pares[chave]:
                return False
            pilha.pop()
    return len(pilha) == 0

def processa_linha(linha):
    if len(linha) > MAX_CARACTERE:
        linha = linha[:MAX_CARACTERE]
        print(f"Atenção: expressão maior que {MAX_CARACTERE} caracteres")
    if linha == "":
        print("ERRO! LINHA VAZIA")
        return
    if bem_formada(linha):
        print("BEM-FORMADA")
    else:
        print("MALFORMADA")

def main():
    print("Digite a expressão: \nPara encerrar, digite 'X' em qualquer posição.")
    for linha in sys.stdin:
        linha = linha.rstrip('\n')
        if 'X' in linha:
            idx = linha.find('X')
            parte = linha[:idx]
            processa_linha(parte)
            break
        else:
            processa_linha(linha)

if __name__ == "__main__":
    main()
