# Lendo um valor em real, a cotação em dolar e imprimindo o valor em dolar

real = float(input('Entre com valor em real(R$): '))
cotacao = float(input('Entre com a cotação do dolar($): '))

conversao = real * cotacao
print(f'O valor R${real} com a cotação atual de R${cotacao}, corresponde ao valor de U${conversao:.2f}')
