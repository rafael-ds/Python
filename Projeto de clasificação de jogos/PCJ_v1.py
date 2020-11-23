# Mini projeto de catalogo de classificação de jogos

catalogo = []


# Função que gera os dados em forma de dict e adiciona no catalogo
def add_itens():
    titulo = str(input('Tilulo do jogo: ').title())
    console = str(input('Console: ').title())
    nota = float(input('Nota dada ao jogo: '))

    dados = {'tilulo': titulo, 'console': console, 'nota': nota}

    catalogo.append(dados)


# Fução opc 1-1 - Retorna a busca no catalogo por titulo.  Caso a lista esteja vazia
# retorna a função add_item()
def buscar_titulo():
    if not catalogo:
        print('Ainda não existe itens em seu catalogo. Deseja adicionar algum item? ')
        add_itens()
    else:
        titulo = str(input('Titulo do jogo: ').title())
        buscar_t = list(filter(lambda t: t['tilulo'] == titulo, catalogo))

        print(buscar_t)


# Fução opc 1-2 - Retorna a busca no catalogo por console.  Caso a lista esteja vazia
# retorna a função add_item()
def buscar_console():
    if not catalogo:
        print('Ainda não existe itens em seu catalogo. Deseja adicionar algum item? ')
        add_itens()

    else:
        console = str(input('Console: ').title())
        buscar_c = list(filter(lambda c: c['console'] == console, catalogo))

        ordem = sorted(buscar_c, key=lambda o: o['nota'], reverse=True)

        for i in ordem:
            print(i)


# Função que retorna a busca no catalogo em ordem crescente da classificação
def busca_crescente():
    if not catalogo:
        print('Ainda não existe itens em seu catalogo. ')


    else:
        classisf = sorted(catalogo, key=lambda c: c['nota'], reverse=True)

        for i in classisf:
            print(i)


# Função que retorna a busca no catalogo em ordem decrescente da classificação
def busca_decrescente():
    if not catalogo:
        print('Ainda não existe itens em seu catalogo. ')

    else:
        classf = sorted(catalogo, key=lambda c: c['nota'])

        for i in classf:
            print(i)


# Menu
while True:

    print('=' * 50 + ' Catalogo de jogos ' + '=' * 59)
    print('1 - Catalogo de jogos -- '
          '2 - Busca -- '
          '3 - Classificação -- '
          '4 - Adicionar item ao catalogo \n'
          '5 - Remover item do catalogo -- ' 
          '6 - Atulizar catalogo -- '
          '7 - sair ')
    print('=' * 128 + '\n')

    opc = str(input('Entre com a opção: '))

    # Visualizar catalogo
    if opc == '1':
        print(' ¨¨¨¨¨ Calalogo ¨¨¨¨¨ ')
        if not catalogo:
            print('Ainda não a item no catalogo.')
        else:
            catal = sorted(catalogo, key=lambda c: c['console'], reverse=True)
            for i in catal:
                print(i)

    # Verificar classificações dos jogos
    elif opc == '2':
        print(' ¨¨¨¨¨ Buscar ¨¨¨¨¨ ')

        buscar = str(input(' 1 - Buscar por titulos -- 2 Buscar por console: '))

        if buscar == '1':
            buscar_titulo()

        elif buscar == '2':
            buscar_console()

        else:
            print('Opção não encontrada! ')

    # Adicionar item ao catalogo
    elif opc == '3':
        print(' ¨¨¨¨¨ classificação ¨¨¨¨¨ ')

        buscar_class = str(input(' 1 - Ordem crescente -- 2 Ordem decrescente: '))

        if buscar_class == '1':
            print('Ordem crescente')
            busca_crescente()

        elif buscar_class == '2':
            print('Ordem decrescente')
            busca_decrescente()

    elif opc == '4':
        print(' ¨¨¨¨¨ Adicionar item ao catalogo ¨¨¨¨¨ ')
        add_itens()

    # Remover itens do catalogo
    elif opc == '5':
        print(' ¨¨¨¨¨ Remover item do catalogo ¨¨¨¨¨ ')

    # Atualizar itens do catalogo
    elif opc == '6':
        print(' ¨¨¨¨¨ Atualizar o catalogo ¨¨¨¨¨ ')

    # sair do programa
    elif opc == '7':
        sair = str(input('Deseja sair do programa? s/n: '))
        if sair == 's':
            print('Saido do programa...')
            break
