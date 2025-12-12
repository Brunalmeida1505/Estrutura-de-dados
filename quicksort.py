import random
def partition(seq, low, high):
    pivot_index = random.randint(low, high - 1)
    pivot = seq[pivot_index] # Valor do pivot
    seq[pivot_index], seq[high - 1] = seq[high - 1],
    seq[pivot_index] # Move o pivot para o final
    i = low # Índice do elemento menor encontrado
    for j in range(low, high - 1):
        if seq[j] < pivot:
            seq[i], seq[j] = seq[j], seq[i] # Troca elementosmenores para a esquerda do pivot
            i += 1
        seq[i], seq[high - 1] = seq[high - 1], seq[i] # Colocao pivot em sua posição correta
        return i
def quicksort(seq):
    def quicksort_helper(seq, low, high):
        if low < high - 1:
            pivot_index = partition(seq, low, high) # Realiza o particionamento
            quicksort_helper(seq, low, pivot_index) # Ordena a sublista à esquerda do pivot
            quicksort_helper(seq, pivot_index + 1, high)
        quicksort_helper(seq, 0, len(seq)) # Chama a funçãoauxiliar para ordenar toda a lista
# Exemplo de uso
numbers = [5, 8, 2, 6, 9, 1, 0, 7]
quicksort(numbers) # Chama a função para ordenar a lista
print(numbers)

