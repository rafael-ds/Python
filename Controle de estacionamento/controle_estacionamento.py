# Programa de cotrole de estacionamento

vagas_rotativo = []
cadastros_rotativo = [
    {'placa': '78r56', 'modelo': 'Corsa', 'cor': 'Preto', 'nome_cliente': 'Rafael'},
]

vips = []
cadastros_vips = []


def tipo_usuario():
    """
    Função que trata do tipo de usuario: se é vip ou casual
    :return:
    """
    # usuario = str(input('Usuario vip? s/n: \n'))
    print(vagas_rotativo)
    usuario = str(input('\nDigite a placa:\n'))

    for lista in range(0, len(cadastros_rotativo)):
        # print(type(cadastros_rotativo[lista]))
        placa_user = cadastros_rotativo[lista].get('placa')

        if usuario == placa_user:
            # Nao esta add nas vagas_torativo
            vagas_rotativo.extend(usuario)
            print(vagas_rotativo)
            #print(f'Usuarios: {vagas_rotativo}\n')

            # Registar a hora de entrada
        else:
            print('Placa não encontrada.\n')
            entrada_rotativo()
            add_vaga()
            print(vagas_rotativo)


def entrada_rotativo():
    novo = str(input('Cadastrar cliente? s/n: '))

    if novo == 's':
        cadastrar()
        print('Cadastro finalizado.\n')

    elif novo == 'n':
        tipo_usuario()
    tipo_usuario()

    """if ficha == 's':
        for clientes in cadastros_rotativo:
            print(clientes)"""


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


def add_vaga():
    """
    Função que add o usuario cadastrado as vagas disponivel
    :return:
    """
    for i in cadastros_rotativo:
        vagas_rotativo.extend(i)


tipo_usuario()
add_vaga()
print(vagas_rotativo)

"""for i in vagas_rotativo:
    print(f'{vagas_rotativo.index(i)} - {i}')"""


