# Agenda de contatos
import time
import ast

contatos = []

print('==' * 20 + ' Agenda Pessoal ' + '==' * 20 + '\n')
acessar = str(input('Deseja acessar sua agenda?\n(s/n):'))

while acessar == 's':
    print('=' * 100)
    print(' 1 - Mostrar contatos.|'
          ' 2 - Add contatos|'
          ' 3 - Buscar contatos|'
          ' 4 - Alterar contatos|'
          ' 5 - Remover contatos|'
          ' 6 - Sair')
    print('=' * 100 + '\n')

    opc = input('Entre com a opção:')

    if opc == '1':
        print('=' * 5 + 'Meus contatos:' + '=' * 5)

        with open('agenda.txt', 'r') as meus_contatos:
            # Transformando 'str' para um iteravel
            buscar = ast.literal_eval(meus_contatos.read())
            for i in buscar:
                print(i)

    elif opc == '2':
        print('=' * 5 + 'Adicionar contato' + '=' * 5)

        with open('agenda.txt', 'a') as minha_agenda:
            while True:
                add = input('Adicionar novo contato? S/N: ')

                if add == 's':
                    nome = str(input('Entre com o nome do contato: ').title())
                    tel = int(input('Entre com o telefone do contato: '))
                    email = str(input('Entre com o e-mail do contato: '))

                    add_contatos = {'nome': nome, 'tel.': tel, 'email': email}

                    # OBS: por ser um 'str' do formato dict() ouve a necessidade de implementar " + ',' "
                    # modificando para tupla
                    minha_agenda.write(str(add_contatos) + ', ')

                    print('...')
                    time.sleep(1.5)
                    print('Contato adicionado com sucesso! \n')

                elif add == 'n':
                    break

    # Buscando contatos
    elif opc == '3':
        print('=' * 5 + 'Buscar contato' + '=' * 5)

        with open('agenda.txt', 'r') as contato:
            # Transformando 'str' para um iteravel
            # OBS: por ser um 'str' do formato dict() ouve a necessidade de implementar " + ',' " modificando para tupla
            dados_dic = ast.literal_eval(contato.read())

            nome_contato = str(input('Entre com o nome do contato: ').title())

            buscar = list(filter(lambda b: b['nome'] == nome_contato, dados_dic))
            print(buscar)

    # Alterando contatos
    elif opc == '4':
        with open('agenda.txt', 'r') as dados:
            alt_dados = ast.literal_eval(dados.read())
            contatos.append(alt_dados)

        nome_contato = str(input('Entre com o nome do contato: ').title())

        for i in contatos:
            item = list(filter(lambda c: c['nome'], i))
            print(f'1 -> Item {item}')
            print(f'2 -> Item {type(item)}')
            print(f'2 -> Item {len(item)}')

            """del item[]"""

            print(f'1 -> Item {item}')
            print(f'2 -> Item {len(item)}')


    elif opc == '5':
        print('Opção não disponivel')

    else:
        if opc == '6':
            sair = str(input('Desaja sair da agenda? (s/n): '))

            if sair == 's':
                print('Saindo da agenda...')
                time.sleep(1.5)
                break

if acessar == 'n':
    print('Saindo da agenda...')
    time.sleep(1.5)
