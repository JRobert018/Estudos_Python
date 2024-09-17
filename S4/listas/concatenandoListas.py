#A concatenação de listas é uma ferramenta que possibilita a junção de várias listas em uma única. há certas formas de fazer isso,como:

lista_A = [10,20,30,40]
lista_B = [50,60,70,80]
lista_C = lista_A+lista_B#forma mais rústica de fazer a concatenação
print(f"Forma rústica:{lista_C}")
lista_A.extend(lista_B)# Esse método é bem eficìente, mas cuidado ao usa-lo,pois o método extend não retorna o valor,evite de atribuir essa forma a uma nova
#variável.

print(f"Forma extend:{lista_A}")