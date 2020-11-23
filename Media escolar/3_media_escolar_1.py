# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
cont = 0
soma = 0

while cont < 4:
    enter_notas = float(input('Entre com a nota do semestre:'))
    notas.append(enter_notas)
    cont += 1

    soma = soma + enter_notas
    media = soma / 4

if media <= 3.0:
    print(f'-> Media: {media} \n-> Aluno reprvado.')
elif 3.0 < media < 6:
    print(f'-> Media: {media}\n-> Aluno em recuperação.')
elif media >= 6:
    print(f'-> Media {media}\n-> Aluno aprovado')