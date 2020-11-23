produtos = 'PlayStation 5'

valor = float(input('Informer o valor do produto:\n'))

vip = input('Cliente vip?\n')
senha = '1234'

if vip == 's':
    enter_senha = input(f'Informe sua senha:\n')
    
    if enter_senha == senha:

        print('Senha aceita:\n')
        desc = (valor * 15) / 100
        total = valor - desc

        print(f'{produtos}.\n Valor total com descontor de R${desc}.\n Total a ser pagor R${total}')

    else:
        print('Senha incorreta.')
else:
    print(f'{produtos}. \nValor total a ser pago: R${valor}')
