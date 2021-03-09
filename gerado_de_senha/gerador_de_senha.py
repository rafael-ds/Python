import string
import csv
from time import sleep
from random import choice

letra = string.ascii_letters
numeros = string.digits
caracteres = '_@$&'

concat = letra + numeros + caracteres
temp = []


class Dados:
    def __init__(self, inst):
        self.__inst = inst

    def inst(self):
        return f'{self.__inst}'


def gerar_senha():
    """
    Função geradora de senha
    :return:
    """

    with open('gerador.csv', 'a', encoding='utf-8', newline='') as gerar:
        cabecalho = ['Instituição', 'Senha']
        escrever = csv.DictWriter(gerar, fieldnames=cabecalho)
        if gerar.tell() == 0:  # Verifica se existe algo escrito na primeira linha
            escrever.writeheader()

        while True:
            entrada = input('Digite o nome da instituição ou (1) Para sair: - ').title()

            dado = Dados(entrada)
            if entrada != '1':
                # Randomização dos elementos
                cont = 0
                while cont < 12:
                    randomizar = choice(concat)
                    temp.append(randomizar)
                    cont += 1

                soldar = ''.join(temp)  # Concatenando as strings da lista temp
                print('Gerando senha...')
                sleep(0.8)
                print(f'Senha para {entrada} gerada com sucesso! ')
                escrever.writerow({'Instituição': dado.inst(), 'Senha': soldar})
                del temp[:]  # Limpando a lista para qua não haja concatecação na gravação
            else:
                break


def ver_senhas():
    """
    Função que mosta as intituições e senhas
    :return:
    """
    with open('gerador.csv', 'r', newline='', encoding='utf-8') as abrir:
        ler = csv.DictReader(abrir)
        for linhas in ler:
            print(linhas)


def busca():
    """
    Função que abre o arquivo e retorna um busca do usuario.
    Caso a busca seja False, o mesmo podera adicionar-lo a lista.
    :return:
    """
    with open('gerador.csv', 'r', encoding='utf-8', newline='') as abrir:
        ler = csv.DictReader(abrir)
        buscar = input('Digite o nome da instituição: \n').title()
        item = list(filter(lambda x: x['Instituição'] == buscar, ler))

        if item:
            print(item)
        else:
            print(f'{buscar} não se encontra na lista.'
                  f' Deseja gerar uma senha para {buscar}? ')

            s_n = input('s/n: ')
            if s_n == 's':
                with open('gerador.csv', 'a', encoding='utf-8', newline='') as gerar:
                    cabecalho = ['Instituição', 'Senha']
                    escrever = csv.DictWriter(gerar, fieldnames=cabecalho)
                    if gerar.tell() == 0:  # Verifica se existe algo escrito na primeira linha
                        escrever.writeheader()

                    # Randomização dos elementos
                    dado = Dados(buscar)
                    cont = 0
                    while cont < 12:
                        randomizar = choice(concat)
                        temp.append(randomizar)
                        cont += 1

                    soldar = ''.join(temp)  # Concatenando as strings da lista temp
                    print('Gerando senha...')
                    sleep(0.8)
                    print(f'Senha para {buscar} gerada com sucesso! ')
                    escrever.writerow({'Instituição': dado.inst(), 'Senha': soldar})
                    del temp[:]  # Limpando a lista para qua não haja concatecação na gravação

# Menu
while True:
    print('=' * 25 + ' GERADOR DE SENHA ' + '=' * 25)
    print('1 - Gerar senha | '
          '2 - Ver senhas | '
          '3 - Buscar por senha | '
          '4 - Sair')

    opc = input('Entre com a opção desejada: ')

    if opc == '1':
        gerar_senha()

    elif opc == '2':
        ver_senhas()

    elif opc == '3':
        busca()

    elif opc == '4':
        print('saindo do gerador senha... ')
        sleep(0.8)
        break

