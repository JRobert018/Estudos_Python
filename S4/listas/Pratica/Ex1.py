"""
Faça um programa de comprar com listas,
O usuário deve ter a possibilidade de inserir,apagar e listar
valores de sua lista.Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os#importa o Sistem operacional
listaDeCompras = []

while True:
   
   opcao = str(input("Selecione uma opção\n[i]nserir [a]pagar [l]istar:")).upper()

   if opcao == "I":
      os.system('clear')#Limpa o terminal antes de executar o bloco de código.
      item = str(input("Informe o item que deve ser adicionado a lista: "))
      listaDeCompras.append(item)
   elif opcao == "A":
      os.system('clear')
      if len(listaDeCompras) == 0:
         print("A lista está vazia.")
      else: 
         remover = int(input("Informe o índice do item a ser removido:"))
         if remover > len(listaDeCompras):
            print("índice inválido,tente novamnete.")
         else:
            itemRemovido = listaDeCompras.pop(remover)
            print(f"O produto {itemRemovido} foi removido")
      
   elif opcao == "L":
      os.system('clear')
      if len(listaDeCompras) == 0:
         print("Não a itens a serem listados.")
      else:
   
         for indice,item in enumerate(listaDeCompras):
            print(indice,item)
   else:
      print("Comando inválido.")
      

   