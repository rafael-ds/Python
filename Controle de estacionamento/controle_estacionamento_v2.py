cadastro_rotativo = []
vaga_rotativo = []

print('==' * 20 + ' Controle de estacionamento ' + '==' * 20 + '\n')

# Inicialização do app
iniciar_app = str(input('Iniciar programa? s/n: '))


# Função de entrada de dados
def dados_cliente():
    placa = str(input('Placa dados: '))
    modelo = str(input('Modelo: '))
    cor = str(input('Cor: '))
    cliente = str(input('Nome cliente: '))

    dados = {'placa': placa, 'modelo': modelo, 'cor': cor, 'Nome cliente': cliente}

    cadastro_rotativo.append(dados)
    vaga_rotativo.append(dados)


def saida():
   """ placa = str(input('Placa saida: '))

    print('ok')



    user_saida = list(filter(lambda us: us['placa'] == placa, vaga_rotativo))
    for u in user_saida:
        vaga_rotativo.remove(u)"""


"""def entrada():
    placa = str(input('Placa entrada: '))

    user = list(filter(lambda u: u['placa'] == placa, cadastro_rotativo))
    for i in user:
        vaga_rotativo.append(i)"""


while True:
    if iniciar_app == 's':

        print('=' * 130)
        print(' 1 - Entrada |'
              ' 2 - Saida |'
              ' 3 - Cadastros Rotativo |'
              ' 4 - Vagas Rotativo |'
              ' 5 - Sair |')
        print('=' * 130 + '\n')

        opc = int(input('Entre com a opção: '))

        if opc == 1:
            if not cadastro_rotativo:
                dados_cliente()
            else:
                placa_comparacao = str(input('placa comparaçao: '))

                for cad_rot in cadastro_rotativo:
                    p_user = cadastro_rotativo[cad_rot].get('placa')

                    if placa_comparacao == p_user:
                        print(p_user)
                    else:
                        dados_cliente()
                        break

                """p_user = list(filter(lambda u: u['placa'] == placa_comparacao, cadastro_rotativo))

                for user in cadastro_rotativo:
                    vaga_rotativo.append(p_user)

                    if not p_user:
                        print('Placa nao cadastrada.')
                        dados_cliente()
                        break"""

        elif opc == 2:
            print('Saida.')
            saida()

        elif opc == 3:
            for i in cadastro_rotativo:
                print(i)

        elif opc == 4:
            for i in vaga_rotativo:
                print(i)

    else:
        break
