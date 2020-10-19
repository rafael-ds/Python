# Calculando a media aritimetica de 4 notas

notas = []
cont = 0

while cont < 4:
    entre_notas = float(input('Entre com a nota do aluno: '))
    notas.append(entre_notas)
    cont += 1

media = sum(notas) / 4

print(f'Notas do aluno: {notas}')
print(f'Media aritimetica: {media}')