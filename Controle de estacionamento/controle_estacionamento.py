# Programa de cotrole de estacionamento
import time

vagas_rotativo = []
cadastros_rotativo = []

historicos = []

vips = []
cadastros_vips = []

print('==' * 20 + ' Controle de estacionamento ' + '==' * 20 + '\n')

# Inicialização do app
iniciar_app = str(input('Iniciar programa? s/n: '))


def tipo_usuario():
    """
    Função que trata do tipo de usuario: se é vip ou casual
    :return:
    """

    user = str(input('Usuario vip?\ns/n:  '))

    if user == 's':
        print('Bem vindo vip!')  # Logica ainda não programada

    # Chamada da função usuario_rotativo()
    else:
        usuario_rotativo()


def usuario_rotativo():
    """
    Função que trata do usuario rotativo
    :return:
    """

    # Verificação se lista vagas_rotativo é maior 99 itens
    for vagas in vagas_rotativo:
        if len(vagas) > 99:
            return 'Não a vagas'

    # if not -> Verificando se a lista esta vazia
    if not cadastros_rotativo:
        entrada_rotativo()

    # Entranda de cliente
    else:
        placa_user = str(input('Entre com a placa do carro: '))

        # Verificação se a placa do cliente esta no cadastro e
        for cadastros_rot in range(0, len(cadastros_rotativo)):
            user = cadastros_rotativo[cadastros_rot].get('placa')

            # Caso esteja adicionar na vaga.
            if user == placa_user:
                print(f'Cod-Cliente: {cadastros_rot} - {cadastros_rotativo[cadastros_rot]}')
                vagas_rotativo.append(cadastros_rotativo[cadastros_rot])

            # Caso nao esteja fazer cadastro.
            elif user != placa_user:
                placa = list(filter(lambda u: u['placa'] == placa_user, ))
                print('Cliente não cadastrado! ')
                entrada_rotativo()


def entrada_rotativo():
    novo = str(input('Cadastrar cliente? s/n: '))

    if novo == 's':
        cadastrar()
        print('Cadastro finalizado.\n')
    elif novo == 'n':
        print('Cancelando...')


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
    vagas_rotativo.append({'placa': placa, 'modelo': modelo, 'cor': cor, 'nome_cliente': nome_cliente})


def saida_rotativo():
    """
    Função sem retorno que remove da lista vagas_rotativo
    Adiciona na lista historicos os dados do carro.
    :return:
    """
    if not vagas_rotativo:
        print(f'Não a carros nas vagas.\n{vagas_rotativo}')
    else:
        placa_saida = str(input('Entre com a placa do carro: '))

        for saida in range(0, len(vagas_rotativo)):

            saida_user = vagas_rotativo[saida].get('placa')

            if placa_saida == saida_user:

                historicos.append(vagas_rotativo[saida])
                vagas_rotativo.remove(vagas_rotativo[saida])


def sair():
    return 'Saindo do programa...'


# Loop infinito do menu
while True:
    if iniciar_app == 's':

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
            print('Entrada de clientes: ')
            tipo_usuario()

        elif opc == '2':  # Saida
            print('Saida de clientes: ')
            saida_rotativo()

        elif opc == '3':  # Cadastros Vips
            print('Cadastrar vip: ')

        elif opc == '4':  # Cadastros Rotativo
            print('Lista de cadastros do rotativo: ')

            if not cadastros_rotativo:
                print('Não a cliente cadastrado')

            else:
                for i in cadastros_rotativo:
                    print(f'Cliente: {i}')

        elif opc == '5':  # Vagas Vips
            print('Lista das vagas vips: ')

            print(vagas_rotativo)

        elif opc == '6':  # Vagas Rotativo
            # print(vagas_rotativo)
            print('Vagas do rotativo: ')
            if not vagas_rotativo:
                print('Não há vagas ocupada! ')

            else:
                for i in vagas_rotativo:
                    print(f'Vaga numero: {vagas_rotativo.index(i)} - Dados: {i}')

        elif opc == '7':  # Sair
            sair()

    elif iniciar_app == 'n':
        break
