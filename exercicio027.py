# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. 

nome = str(input("Digite seu nome completo: ")).strip()
nomel = nome.split()
print(f"Primeiro nome: {nomel[0]}")
print(f"Último nome: {nomel[-1]}")