import random
import time

palavras = ('casa', 'abelha', 'cachueira', 'porta', 'mesa', 'lixeira', 'cadeado', 'guarda')
sorteio_palavras = random.choice(palavras)  # Pegando palavras aleatorias
letras = []
tentantiva = 5

acertou = False

print('='*20 + ' JOGO DA FORCA ' + '='*20 + '\n')

print('Sorteando um palavra...')
time.sleep(1.5)  # Criando um pequeno cronometro
print(f'A palavra sorteada possui {len(sorteio_palavras)} letras\n')

# Fazendo um for para substiruir as letras sortiadas por traços
for i in range(0, len(sorteio_palavras)):
    letras.append('-')

# Laço de repetição que executara enquanto
while acertou == False:
    enter_letras = str(input('Entre com uma letra: '))

    # Pecorre a palavra sorteada e inserir a letra acertada
    for i in range(0, len(sorteio_palavras)):
        if enter_letras == sorteio_palavras[i]:
            letras[i] = enter_letras
        print(letras[i])
    acertou = True

    # Pecorre a palavra sorteada e conpara se ainda existe algum taço
    # Caso tenha contunua o laço
    for x in range(0, len(sorteio_palavras)):
        if letras[x] == '-':
            acertou = False

    if enter_letras == sorteio_palavras[i]:
        tentantiva = tentantiva
    else:
        print(f'Você possui {tentantiva} Tentativas.')
        tentantiva -= 1

    # Comparando as tentativas
    if tentantiva <= 0:
        print('enforcado')
        print(letras)
        break

