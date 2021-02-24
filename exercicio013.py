#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite o seu salário: "))
print("Seu novo salário, com o aumento de 15%, é de {:.2f}.".format(salario*1.15))