import random

palavras = ('castelo', 'autodromo', 'musica', 'cachorro', 'paralelepipido', 'videogame', 'papelao'
            'televisao', 'uniforme', 'aviao')

com_palavras = random.choice(palavras)
letras_escolidas = []

tentativas = 6
pontuacao = 0

for plv in range(0, len(com_palavras)):
    letras_escolidas.append('-')

acerto = False

print('='*20 + ' Jogo da Forca ' + '='*20 + '\n')

print(f'A palavra sorteada possui {len(com_palavras)} letras.')
print(f'{letras_escolidas} \n')

while acerto == False:
    pedir_letra = str(input('Digite uma letra: '))

    for letra in range(0, len(com_palavras)):
        if pedir_letra == com_palavras[letra]:
            letras_escolidas[letra] = pedir_letra
            pontuacao += 1

        print(letras_escolidas[letra])
    acerto = True

    for traco in range(0, len(com_palavras)):
        if letras_escolidas[traco] == '-':
            acerto = False


    print(f'Você possui {tentativas} tentativas')

    if tentativas == 0:
        print('Você foi enforcado!')
        print(f'Você fez {pontuacao} pontos!')
        break

print(f'Parabéns! Você fez {pontuacao} pontos.')