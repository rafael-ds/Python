senha = '1234'
cont = 0

enter_senha = input('Informe sua senha:')

while enter_senha != senha:
    pedido_s = input('Entre com sua senha:')
    cont += 1

    if cont == 3:
        print('Senha bloqueada:')
        break

    if pedido_s == senha:
        print('Senha aceita:')
        break
print('Senha aceita:')
