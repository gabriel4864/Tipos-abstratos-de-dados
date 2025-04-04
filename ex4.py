# Fila
# Exercicio 4 - Criar uma implementação simples de uma fila (Queue) usando listas.

# Importando collections.deque para o uso de fila
from collections import deque

#Iniciando uma fila vazia 
fila  = deque()

# Enfileirar elementos
fila.append(20)
fila.append(50)
fila.append(82)
print(fila)

# Mostrar o primeiro elemento da fila
print("Primeiro elemento da fila: ", fila[0])

# Desinfileirando o primeiro elemento
print("Removido: ", fila.popleft())
print(fila)

print("Removido: ", fila.popleft())
print(fila)

#Verificar se a lista está vazia 
print("pilha está vazia: ", len(fila)==0) # Verifica se a lista esta vazia

