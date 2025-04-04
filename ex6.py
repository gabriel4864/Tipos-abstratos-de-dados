# Exercicio 6 - Uma impressora trabalha com um sistema de fila para processar documentos
# enviados para impressão. Cada documento enviado entra no final da fila e será
# impresso na ordem em que chegou.

# Importando collections.deque para o uso de fila
from collections import deque

#Iniciando uma fila vazia 
fila  = deque()

# Enfileirar elementos
fila.append("Copia RG")
fila.append("Copia CPF")
fila.append("Copia Certidão de nascimento")

# Mostrar o primeiro elemento da fila
print("Primeia impressão da fila: ", fila[0])

# Desinfileirando o primeiro elemento
print("Removido: ", fila.popleft())
print("Primeira impressão da fila: ", fila[0]) 

print("Ainda há documentos para imprimir?: ", len(fila)==0)
print("Ordem de impressão: ", fila)