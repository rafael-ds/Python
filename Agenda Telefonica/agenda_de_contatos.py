# Agenda de contatos
import time
import ast

contatos = []
temp = []
cast = []

lixeira = []


# Classe que contem o medoto para instanciar o objeto
class Agenda:

    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email


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

        while True:
            add = input('Adicionar novo contato? S/N: ')

            if add == 's':
                nome_contato = input('Insira o nome do contato: ')
                tel = input('Insira o telefone do contato: ')
                e_mail = input('Insira o email do contato: ')

                user = Agenda(nome_contato, tel, e_mail)

                contatos.append([user.nome])
                contatos.append([user.telefone])
                contatos.append([user.email])

                with open('agenda.txt', 'a') as guardar:
                    guardar.write(str(contatos))
                print(contatos)

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
        with open('agenda.txt', 'r') as abrir:
            dados = ast.literal_eval(abrir.read())
            temp.append(dados)

        for i in temp:
            for n in i:
                cast.append(n)

        nome = input('Informe o nome do contato: ')
        for i in cast:
            if nome == i[0]:
                print(i)
                excluir = input('Deseja excluir esse contato? S/N: ')
                if excluir == 's':
                    dado = i
                    lixeira.append(dado)
                    cast.remove(i)
        with open('agenda.txt', 'w') as atulizar:
            atulizar.write(str(cast))

        print('==' * 100 + 'Prença os dadoa para atualizar seu contato' + '==' * 100)
        nome = input('Insira o nome do contato: ')
        tel = input('Insira o telefone do contato: ')
        e_mail = input('Insira o e-mail do contato: ')

        user = Agenda(nome, tel, e_mail)

        contatos.append(user.nome)
        contatos.append(user.telefone)
        contatos.append(user.email)

        with open('agenda.txt', 'a') as guardar:
            guardar.write(str(contatos) + ',')

    elif opc == '5':
        with open('agenda.txt', 'r') as abrir:
            dados = ast.literal_eval(abrir.read())
            temp.append(dados)

        for i in temp:
            for n in i:
                cast.append(n)

        nome = input('Informe o nome do contato: ')
        for i in cast:
            if nome == i[0]:
                print(i)
                excluir = input('Deseja excluir esse contato? S/N: ')
                if excluir == 's':
                    dado = i
                    lixeira.append(dado)
                    cast.remove(i)
                    print('Removendo contato...')
                    time.sleep(1.5)
                    print('Contato removido com sucesso... ')
                    break
                elif excluir == 'n':
                    break

        with open('agenda.txt', 'w') as atulizar:
            atulizar.write(str(cast))

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
