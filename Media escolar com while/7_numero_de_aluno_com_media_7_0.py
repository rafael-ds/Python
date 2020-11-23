# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

aluno = 0
notas = 0

nome_aluno = []
media = []

while aluno < 3:
    nome = input('Nome do aluno(a):')
    nome_aluno.append(nome)

    nota1 = float(input('Entre com a nota do 1º semestre: '))
    nota2 = float(input('Entre com a nota do 2º semestre: '))
    nota3 = float(input('Entre com a nota do 3º semestre: '))
    nota4 = float(input('Entre com a nota do 4º semestre: '))

    soma = nota1 + nota2 + nota3 + nota4
    notas = (notas + soma) / 4
    media.append(notas)

    print(f'O aluno(a): {nome} tem a media: {notas}\n')

    aluno += 1

for i in media:
    if i >= 7:
        print(f'As medias maiores que 7.0 foram: {i}')



