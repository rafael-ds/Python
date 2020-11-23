# Faça um Programa que introduza em um vetor 5 números inteiros e mostre-os e someos.

vetor = []
cont = 0
soma = 0

print(vetor)

while cont < 5:
    num = int(input('Entre com o numero:'))
    cont += 1
    vetor.append(num)

    soma = soma + num

print(vetor)
print(soma)

