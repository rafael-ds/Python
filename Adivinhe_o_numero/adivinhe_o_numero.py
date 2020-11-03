# Jogo de adivinhação de numero

from random import choice
import time

com = choice(range(1, 100))

print('='*30 + ' Adivinhe o numero ' + '='*30)
print('Buscando por um numero entre 1 e 100...')
time.sleep(1.5)
print('Numero encontrado. Tente adivinha-lo.\n')


def num():
    """
    Uma pequena função que tem como objetivo a comparação da variavel(int) COM e a variavel(int) JOGADOR
    :return: Não possui retorno
    """

    tentaivas = 0
    pontuacao = 100

    global com  # chamada global da variavel n para dentro do escopo da função

    while tentaivas < 10:

        jogador = int(input('Entre com o numero: '))

        if jogador < com:
            pontuacao -= 5
            print(f'Numero errado. Tente um valor maior.\nSua Pontação é {pontuacao}\n')

        elif jogador > com:
            pontuacao -= 5
            print(f'Numero errado. Tente um valor menor. Sua Pontação é {pontuacao}\n')
        else:
            print(f'Parabéns você acertou o numero! Vecê fez {pontuacao} pontos\n')
            break

        tentaivas += 1

    if tentaivas >= 10:
        print(f'Suas tentativas acabaram. Vecê fez {pontuacao} pontos')
        print(f'O numero sortiado era {com}')


num()
