#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite o preço do produto: "))
print("O novo preço com desconto é R${:.2f}.".format(preco*.95))