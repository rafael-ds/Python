# Peça ao usuario para digitar 3 numero e retorne a somas de ambos

"""num1 = int(input('Entre com um numero: '))
num2 = int(input('Entre com um numero: '))
num3 = int(input('Entre com um numero: '))

soma = num1 + num2 + num3
print(soma)"""

nums = []
cont = 0

while cont < 3:
    numeros = int(input('Entre com um numero: '))
    nums.append(numeros)
    cont += 1

soma = sum(nums)
print(f'A somas dos numeros {nums} é: {soma}')
#fim