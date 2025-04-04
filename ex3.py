# EX3 = Você foi contratado para desenvolver uma funcionalidade de “Desfazer/Refazer"
# para um editor de texto simples. O editor permite que o usuário escreva palavras
# em um documento, e, caso cometa um erro, pode desfazer a última ação ou
# refazê-la caso mude de ideia.

pilha = []
print(pilha)

texto = input("Digite o texto: ")
pilha.append(texto)
print("Texto: ")

def desfazer():
  if pilha:
    print("Texto excluido: ", pilha.pop())
    if pilha:
      return "Texto: " + pilha[-1]
    else:
      return  "Fim da edição"

def refazer():
  escrita = input("Digite o novo texto: ")
  pilha .append(escrita)
  return "Texto: " + pilha[-1]

voltar = input("Deseja apagar o texto escrito? [S/N]").upper().strip()
if voltar == "S":
    print(desfazer())  
else:
    print("Texto: " + pilha[-1])
refazer_texto = input("Deseja refazer? [S/N]").upper().strip()
if refazer_texto == "S":
        print(refazer())  
else:
    print("Texto: " + pilha[-1])
