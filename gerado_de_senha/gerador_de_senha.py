import string
import csv
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
                escrever.writerow({'Instituição': dado.inst(), 'Senha': soldar})
                del temp[:]  # Limpando a lista para qua não haja concatecação na gravação
            else:
                break


def ver_senhas():
    with open('gerador.csv', 'r', newline='', encoding='utf-8') as abrir:
        ler = csv.DictReader(abrir)
        for linhas in ler:
            print(linhas)


def buscar_senha():
    with open('gerador.csv', 'r', newline='', encoding='utf-8') as abrir:
        ler = csv.reader(abrir)
        buscar = input('Digite o nome da instituição: \n').title()
        for i in ler:
            if i[0] == buscar:
                print('Instituição | Senha')
                print(i)


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
        buscar_senha()

    elif opc == '4':
        print('saindo do gerador senha')
        break

