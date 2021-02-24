#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 

n = float(input("Quanto você tem na carteira?"))
dolar = n/5.42
print("Com R${} você pode comprar ${}.".format(n, dolar))