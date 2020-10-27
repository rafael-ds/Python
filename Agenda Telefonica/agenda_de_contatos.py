# Agenda de contatos
import time

contatos = []

print('==' * 20 + ' Agenda Pessoal ' + '==' * 20 + '\n')
acessar = str(input('Deseja acessar sua agenda?\n(s/n):'))

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

        add_contatos = {'nome': nome, 'tel.': tel, 'email': email}
        contatos.append(add_contatos)

        time.sleep(1.5)
        print('Contato adicionado com sucesso! \n')

    elif opc == '3':
        # Pecorre a lista trazendo a posição do index e o elemento
        for pos in contatos:
            print(f'{contatos.index(pos)}: {pos}')

        posicao = int(input('\nEntre com a posição do contato:\n '))
        print(f'{posicao}: {contatos[posicao]}')

        alterar = str(input('Deseja alterar esse contato? s/n:\n '))

        if alterar == 's':
            nome = str(input('Entre com o nome do contato: '))
            tel = int(input('Entre com o telefone do contato: '))
            email = str(input('Entre com o e-mail do contato: '))

            contatos[posicao] = {'nome': nome, 'tel.': tel, 'E-mail': email}  # altera o contato na posição escolida
            time.sleep(1.2)
            print('Contato atualizado com sucesso!\n')

    elif opc == '4':
        # Erro ao tentar excluir um item da lista
        # list assignment index out of range
        for pos in contatos:
            print(f'{contatos.index(pos)}: {pos}')

        posicao = int(input('Entre com a posição do contato: '))

        alterar = str(input('Deseja realmente excluir esse contato? '))

        if alterar == 's':
            for i in range(0, len(contatos)):
                contatos[i] = contatos.pop(posicao)
            print(f'{contatos}\nContatos excluido com sucesso!')

    else:
        if opc == '5':
            sair = str(input('Desaja sair da agenda? (s/n): '))

            if sair == 's':
                print('Saindo da agenda...')
                time.sleep(1.5)
                break

if acessar == 'n':
    print('Saindo da agenda...')
    time.sleep(1.5)
