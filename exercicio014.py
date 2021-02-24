#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperatura = float(input("Digite a temperatura em celsius: "))
print("{} ºC equivalem a {:.1f}º fahrenheit.".format(temperatura, temperatura*1.8+32))