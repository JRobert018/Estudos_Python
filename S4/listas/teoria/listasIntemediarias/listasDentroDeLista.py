"""
Listas dentros de listas ou listas aninhada é utilizada para junção de vários tipos de listas e para criação
de matrizes,tabelas e em algumas ocasiões árvores.
""" 
#Essa lista tem 3 listas dentro dela, cada lista recebe seu índice na ordem e cada item dentro da lista também recebe.
salas = [
    #0         1        3
   ['Beto','Vinicius','Carlos'],#0
#     0
   ['Luiz'],#1
#     0       1        2      3
   ["Alana",'Amanda','Bia','Ellen']#2
]

#Para acessar um item especifico de uma das listas devo informa todos seus índices.
print(salas[2][3])#çNesse caso quero que mostre o aluno(a) que esteja na posição 3 da lista 2. Sempre informe índice externo para o interno.
print('---'*30)

#Podemos usar o for dentro de for para ler o conteudo dessas listas.
for sala in salas:
   for aluno in sala:
      print(aluno)