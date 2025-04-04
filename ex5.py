# Exercicio 5 - Um consultório odontológico precisa gerenciar a ordem de atendimento dos
# pacientes. Para isso, foi decidido implementar uma fila onde os pacientes são
# chamados na ordem em que chegaram (FIFO – First In, First Out).

# Importando collections.deque para o uso de fila
from collections import deque

#Iniciando uma fila vazia 
fila  = deque()

# Enfileirar elementos
pessoas = int(input("Digite quantas pessoas chegaram ao consultório: "))
for i in range (pessoas):
    nomes = input("Digite o nome do cliente por ordem de chegada (Do primeiro cliente ao ultimo a chegar): ")
    fila.append(nomes)

print("Essa é a ordem de atendimento: ", fila)

