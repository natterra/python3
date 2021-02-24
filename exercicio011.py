#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = altura*largura

print("Você irá precisar de {} litros de tinta para pintar os {} m2 de parede.".format(area/2, area))