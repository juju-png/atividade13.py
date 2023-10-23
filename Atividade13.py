# Exercício Python 14: Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.
n1,n2,n3=float(input("numero 1: ")),float(input("numero 2: ")),float(input("numero 3: "))
numeros=[n1,n2,n3]
print(f"maior: {max(numeros)}")
print(f"menor: {min(numeros)}")

