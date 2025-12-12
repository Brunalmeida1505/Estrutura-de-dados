from collections  import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

print("Pilha inicial")
print(stack)

print('\bElementos removids da pilha')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nPilha após retirada dos elementos')
print(stack)
