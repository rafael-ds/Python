# Agenda de contatos

import time

print('==' * 20 + ' Agenda Pessoal ' + '==' * 20 + '\n')

print('Deseja acessar sua agenda? ')

contatos = [
    {'nome': 'Mae', 'tel.': 90165634, 'E-mail': 'dinha@gmail.com'},
    {'nome': 'Raquel', 'tel.': 2254178, 'E-mail': 'nat@gmail.com'}
]

acessar = str(input('(s/n):'))

while acessar == 's':
    print('=' * 100)
    print(' 1 - Mostrar contatos.|'
          ' 2 - Add contatos|'
          ' 3 - Alterar contatos|'
          ' 4 - Remover contatos|'
          ' 5 - Sair')
    print('=' * 100 + '\n')

    opc = input('Entre com a opção:')

    if opc == '1':
        print('Meus contatos:')
        for i in range(0, len(contatos)):
            print(contatos[i])

    elif opc == '2':
        nome = str(input('Entre com o nome do contato: '))
        tel = int(input('Entre com o telefone do contato: '))
        email = str(input('Entre com o e-mail do contato: '))

        add_contatos = {'nome': nome, 'tel.': tel, 'E-mail': email}
        contatos.append(add_contatos)

        time.sleep(1.5)
        print('Contato adicionado com sucesso! \n')

    elif opc == '3':
        # Pecorre a lista trazendo a posição do index e o elemento
        for pos in contatos:
            print(f'{contatos.index(pos)}: {pos}')

        posicao = int(input('\nEntre com a posição do contato: '))
        print(f'{posicao}: {contatos[posicao]}')

        alterar = str(input('Deseja alterar esse contato? s/n:\n '))

        if alterar == 's':
            nome = str(input('Entre com o nome do contato: '))
            tel = int(input('Entre com o telefone do contato: '))
            email = str(input('Entre com o e-mail do contato: '))

            contatos[posicao] = {'nome': nome, 'tel.': tel, 'E-mail': email} # altera o contato na posição escolida
            time.sleep(1.2)
            print('Contato atualizado com sucesso!\n')


    elif opc == '4':
        for i in contatos:
            print(contatos)
            # Nao encontrando alogica para a remoção

if acessar == 'n':
    print('Saindo da agenda...')
    time.sleep(1.5)
