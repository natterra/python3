#Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input("Digite um número: "))
i = 0
print("-----------")
while i < 10:
    i += 1
    print(f"{n} x {i} = {n*i}")
print("-----------")