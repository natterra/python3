# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input("Digite uma frase: ")
frase = frase.upper().strip()
qde = frase.count('A')
print(f"A letra A aparece {qde} vezes.")
print(f"A letra A aparece a primeira vez na posição {frase.find('A')+1}")
print(f"A letra A aparece a ultima vez na posição {frase.rfind('A')+1}")