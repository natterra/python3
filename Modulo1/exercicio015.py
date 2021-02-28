#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Quantidade de km: "))
dias = int(input("Quantidade de dias: "))
print("O valor a pagar é de R$ {:.2f}".format(60*dias + km*.15))