# Exercicio 7 - Uma central de atendimento telefônico gerencia chamadas em espera usando
# uma pilha. Isso significa que a última chamada recebida será a primeira a ser
# atendida.
pilha = []
print(pilha)

#Empilhando elementos
pilha.append(11956166616)
pilha.append(11965165161)
pilha.append(11951316646)
print(pilha)

print("Primeira chamada a ser atendida: ", pilha[-1]) # Traz o ultimo elemento presente na variável

#Remover item que está no topo
print("Atendida: ", pilha.pop()) # Remove o item que está no topo 
print("Ordem de atendimento ", pilha)

print("A lsita de chamada está vazia?: ", len(pilha)==0) # Verifica se a lista esta vazia
