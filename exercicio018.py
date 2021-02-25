#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 

import math
a = float(input("Digite um ângulo: "))
print("O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.".format(math.sin(math.radians(a)), math.cos(math.radians(a)), math.tan(math.radians(a))))