#Pilha 
#Exercício 2 - Criar uma pilha e manipular seus elementos.
pilha = []
print(pilha)

#Empilhando elementos
pilha.append(20)
pilha.append(10)
pilha.append(15)
print(pilha)

print("Topo da pilha: ", pilha[-1]) # Traz o ultimo elemento presente na variável

#Remover item que está no topo
print("Removido: ", pilha.pop()) # Remove o item que está no topo 
print(pilha)

print("Removido: ", pilha.pop()) # Remove o item que está no topo 
print(pilha)

print("Removido: ", pilha.pop()) # Remove o item que está no topo 
print(pilha)

print("pilha está vazia: ", len(pilha)==0) # Verifica se a lista esta vazia