# Programa para imprimir a quantia liquida de um contratado
# Diaria R$30, Descontos 8%

diaria = int(30)
dias_trab = int(input('Entre com os dias trabalhados: '))

bruto = diaria * dias_trab
liquido = (bruto * 8) / 100

print(f'O valor a ser pago pelos dias de trabalho sera de: R${bruto - liquido}')
