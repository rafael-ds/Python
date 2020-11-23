# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.

vetor = []
v_par = []
v_inpar = []
cont = 0

while cont < 20:
    num = int(input('Entre com um numero: '))
    vetor.append(num)
    cont += 1

    if (num % 2) == 0:
        v_par.append(num)
    else:
        v_inpar.append(num)

print(f'Elementos do vetor:\n{vetor}')
print(f'Elementos pares do vetor:\n{v_par}')
print(f'Elementos impares do vetor:\n{v_inpar}')

print(f'O vetor tem um total de {len(vetor)} elementos.')
