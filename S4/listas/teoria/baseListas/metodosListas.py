"""                                 C     R     U     D
Ainda em uma lista podemos fazer o crat read update delete

Sobre os métodos das lista temos append(adciona um item ao final da lista), insert(subtituir um item da lista por outro),pop(remove o item),del(deleta)
clear(limpa o conteido da lista), extend(extende a lista).
"""
listaTeste = [10,20,35,70]
listaTeste[3] = 55#Isso é uma alteração no conteudo da lista, indepedente de onde eu chamar ela a alteração continua.
del listaTeste[1] #Com isso deletamos o conteudo do índice informado, e os índices serão realocados.E isso usa muito processamento em lista gigantes
#devemos evitar essa realocação de índices.
print(listaTeste)
listaTeste1 = [20,45,56,90]

listaTeste1.append("novo item")#o dado é inserido ao final da lista. 
listaTeste1.append(1)
print(listaTeste1)

listaTeste1.pop()#Quando não houver paramêtros ao pop ele remove o ultimo item da lista.
#evite de fazer isso em listas gigantes!!!

listaTeste1.pop(2)#já quando houver ele remove o item do índice informado. 
print(listaTeste1)


listaTeste2 = [25,15,76,98]
print(listaTeste2)
#                  I dado
listaTeste2.insert(1,51)#O inset insere um elmento no índeci que é informado em seus paramêtros.
print(listaTeste2)