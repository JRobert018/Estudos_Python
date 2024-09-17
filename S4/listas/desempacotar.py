"""
Desempacotamento em python permite extrair os elementos de uma lista ou tuplas e atribuí-las a variáveis individuais.
"""
lista = [1,2,3]
a,b,c = lista#Ele separa os dados da lista e os atribui em variáveis separadas,seguindo a ordem dos índices.
print(a)
print(b)
print(c)

#Esse tipo de desempacotamento tem o probelma de só funcionar se as váriaveis e índices serem totalmente atendidos.
#Mas para resolver isso temos como usar um método que pegue variáveis especificas e deixe uma variável com o resto.

lista2 = ["beto","luiz","douglas"]
#se adcionamor uma "_" antes da váriavel que iremos usar, ele ignora os antecessores da variável.
_,nome2,*_ = lista2# em ocasiões que não usaremos o resto da lista é um bom custume usar só o "_" para representa-lo, isso significa 
#que ele não deve ser usado.
print(nome2)
print(_)