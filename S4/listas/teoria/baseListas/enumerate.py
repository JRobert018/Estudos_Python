#A função enumerate serve para enumerar todos os índices de uma lista.Criando uma tupla com o índice + conteudo da lista.
lista = ["João","Marcos","Marcio","Maria","Luiz"]
#Se usar o enumerate fora de um laço de repetição, ele irá apresentar seu endereço de mémoria.
print("Método mais apresentavel:")
for item,nome in enumerate(lista):
   print(item,nome)
print('----'*30)
print("Método tupla:")
for i in enumerate(lista,start=2):#Podemos começar a enumeração por pontos especificados pelo dev
   print(i)