#  Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

# – O nome com todas as letras maiúsculas e minúsculas.

# – Quantas letras ao todo (sem considerar espaços).

# – Quantas letras tem o primeiro nome.

nome = input("Digite o nome: ")
nome2 = nome.split()
tamanho = len("".join(nome2))
print(nome.lower())
print(nome.upper())
print(f"Ao todo esse nome tem {tamanho} letras.")
print(f"{nome2[-1]} tem {len(nome2[-1])} letras.")