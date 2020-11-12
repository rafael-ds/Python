# Programa de cotrole de estacionamento

vagas_rotativo = []
cadastros_rotativo = [
    {'placa': '78r56', 'modelo': 'Corsa', 'cor': 'Preto', 'nome_cliente': 'Rafael'},
    {'placa': '985t3', 'modelo': 'Fusion', 'cor': 'Verde', 'nome_cliente': 'Edna'}
]

vips = []
cadastros_vips = []


print('==' * 20 + ' Controle de estacionamento ' + '==' * 20 + '\n')

iniciar_app = str(input('Iniciar programar? s/n: '))


def inicia_app():
    if iniciar_app == 's':
        # Menu de opção
        print('=' * 130)
        print(' 1 - Entrada |'
              ' 2 - Saida |'
              ' 3 - Cadastros Vips |'
              ' 4 - Cadastros Rotativo |'
              ' 5 - Vagas Vips |'
              ' 6 - Vagas Rotativo |'
              ' 7 - Sair |')
        print('=' * 130 + '\n')

        opc = str(input('Entre com a opção desejada: '))

        if opc == '1':  # Entrada
            # tratamedo para verificar se ha vagas no rotativo
            tipo_usuario()

            inicia_app()

        elif opc == '2':  # Saida
            print('ok')
            inicia_app()

        elif opc == '3':  # Cadastros Vips
            inicia_app()

        elif opc == '4':  # Cadastros Rotativo
            for i in cadastros_rotativo:
                print(f'{cadastros_rotativo.index(i)} - {i}')
            inicia_app()

        elif opc == '5':  # Vagas Vips
            print(vagas_rotativo)

        elif opc == '6':  # Vagas Rotativo
            # print(vagas_rotativo)
            for i in vagas_rotativo:
                print(f'Vaga numero: {vagas_rotativo.index(i)} - Placa: {i}')
            inicia_app()

        elif opc == '7':  # Sair
            print('Saindo do programa.')

    elif iniciar_app == 'n':
        print('Saindo do programa.')


def tipo_usuario():
    """
    Função que trata do tipo de usuario: se é vip ou casual
    :return:
    """
    for vagas in vagas_rotativo:
        if len(vagas) > 99:
            print('Não há vagas')
            break

    user = str(input('Usuario vip?\ns/n:  '))

    if user == 's':
        print('Bem vindo vip!')
    return usuario_rotativo()


def usuario_rotativo():
    """
    Função que trata do usuario rotativo
    :return:
    """

    usuario = input('\nDigite a placa:\n')

    for lista in range(0, len(cadastros_rotativo)):
        placa_user = cadastros_rotativo[lista].get('placa')

        if usuario == placa_user:
            print(cadastros_rotativo)
            vagas_rotativo.append(usuario)
            inicia_app()

            # Registar a hora de entrada
        elif usuario != placa_user:
            print(cadastros_rotativo)

            print('Placa não encontrada.\n')
            entrada_rotativo()
            vagas_rotativo.append(usuario)

            print(cadastros_rotativo)
            inicia_app()


def entrada_rotativo():
    novo = str(input('Cadastrar cliente? s/n: '))

    if novo == 's':
        cadastrar()
        print('Cadastro finalizado.\n')

    elif novo == 'n':
        inicia_app()


def cadastrar():
    """
    Função que trada do dados so usuario adicionando-os na lista cadastro_rotativo
    :return:
    """
    placa = str(input('Informe a placa do veiculo: '))
    modelo = str(input('Informe o modelo do veiculo: ').title())
    cor = str(input('Informe a cor do veiculo: ').title())
    nome_cliente = str(input('Informe o nome do cliente: ').title())

    cadastros_rotativo.append({'placa': placa, 'modelo': modelo, 'cor': cor, 'nome_cliente': nome_cliente})


inicia_app()


