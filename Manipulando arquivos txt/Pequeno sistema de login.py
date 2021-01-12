"""
Pequeno sistema de login de usuario desenvolvido afim de apredizagem.

"""


def cadastro():
    print('Cadastrar usuario.')

    # Criando um arquivo .txt com o nome escolhido pelo usuario
    with open('nick.txt', 'w') as nick_user:
        nick = str(input('Entre com um nick: '))
        nick_user.write(nick)

    # Criando um arquivo .txt com a senha escolhido pelo usuario
    with open('pass.txt', 'w') as pass_user:
        pass_u = str(input('Entre com uma senha: '))
        pass_user.write(pass_u)

    print('Usuario cadastrado com sucesso! ')


def login():
    # Lendo e comparando arquivo .txt com o nome escolhido pelo usuario
    with open('nick.txt', 'r') as nick_user:
        nick = str(input('Entre com seu nick: '))

        if nick == nick_user.read():
            print('...')
        else:
            print('Nick invalido! ')
            menu()

    with open('pass.txt', 'r') as pass_user:
        pass_u = str(input('Entre com sua senha! '))

        if pass_u == pass_user.read():
            user = open('nick.txt', 'r')
            print(f'Seja Bem vindo @{user.read()}\n')
        else:
            print('Senha invalida')
            menu()


def menu():
    while True:
        print('1 - Login == '
              '2 - Cadastrar ')

        # OBS-> Usei opc como "string" pos como "int" estava ocorrendo erro.
        opc = str(input('Entre com a um das opções: '))

        if opc == '1':
            login()

        elif opc == '2':
            cadastro()


menu()
