#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

cateto1 = float(input("Digite o cateto oposto: "))
cateto2 = float(input("Digite o cateto adjacente: "))
hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
print(f"A hipotenusa é {hipotenusa}")