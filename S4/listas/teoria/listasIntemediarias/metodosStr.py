"""
Métodos úteis para mexer com strings,listas e tuplas, resumindo tudo que for iterável.
split e join com listas e strings
O slipit divide uma string
Já o join junta a string
"""

frase = 'Uso do slpit, que legal !'
lista_split = frase.split('!')#podemos colocar paramêtros no split para que ele ignore algum caractere.
print(lista_split)
#Para continuar a formatação das strings,temos o strip() que elimina os espaços do inicio e do fim de uma frase, também temos
# o rstrip() e lstrip() que elimina só os espaços da direita e esquerda respectivamente.
frase2 = "   tem muito espaço livre nessa mensagem   "
print(f"Sem espaços nas pontas: {frase2.strip()}")
print(f"Sem espaços na ponta direita: {frase2.rstrip()}")
print(f"Sem espaços na ponta esquerda: {frase2.lstrip()}")


#Uso do join
lista_join = ["a","b","c"]
frase_unidas = "-".join(lista_join)# ele junta um caractere a sua escolha para juntar com cada índice de uma string ou lista.
print(frase_unidas)