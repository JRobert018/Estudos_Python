"""
Como o tipo list nós permite ter dados mútaveis em nossa lista,devemos tomar alguns cuidados, quando:
copiar valores(imútaveis) e apontar para o mesmo valor na mémoria(mútaveis).

"""
#Quando atribuirmos uma lista para uma nova variável, elas ficam "concectadas" quando uma tiver alteração a outra por consequência terá a mesma alteração.
lista_a = [10,20,30]
lista_b = lista_a

lista_a[0] = 99
lista_b[1] = 55
print(f"Lista_b:{lista_b}")
print(f"lista_a:{lista_a}")

#Mas temos como contorna essa situação usando o comando copy, que como o próprio nome diz ele faz uma copia da lista.

print("---"*30)
lista_1 = ["Roberto","João","Carlos"]
lista_2 = lista_1.copy()#O método copy,cria uma copia da lista que é totalmente independente da original.
lista_2[0] = "Leo"
print(lista_1)
print(f"lista2 usando o 'copy':{lista_2}")

