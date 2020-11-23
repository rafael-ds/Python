valor_gas = float(input('Informe o valor da gasolina:\n'))
litros_gas = float(input('Informe a quantidade de litros desejado:\n'))

quil_por_litro = int(input('Entre com KM por litro de gasolina gasto pelo veiculo:\n'))

total_pg = valor_gas * litros_gas
km = quil_por_litro * litros_gas

print(f'O valor total a ser pagor pela gasolina sera de:\n R${total_pg}\n')
print(f'Você podera pecorrer ate {km}KM')



