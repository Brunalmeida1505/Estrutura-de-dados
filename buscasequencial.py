def busca_sequencial(A, chave, N):
    for i in range(0,N):
        if (A[i] == chave):
            return A[i]
    return "chave não encontrada"

lista = []
for lista in range (0,10):
    busca_sequencial()