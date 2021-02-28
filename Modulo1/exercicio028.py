# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

i = 0
lista = []
while i < 6:
    lista.append(i)
    i += 1
num = int(input("Digite um número entre 0 e 5: "))
numpc = random.choice(lista)
print(f"O computador escolheu {numpc}.")
if num == numpc:
    print("Você venceu!")
else:
    print("Você perdeu!")