# Pograma que da um desconto de 12 porcento de um produto

produto = 'Video Game'
valor = float(input('Entre com o valor do produto: R$'))

desc = (valor * 12) / 100

print(f'Produto: {produto}.\nValor: R${valor}\nDesconto: R${desc}\nTotal a pagar: R${valor - desc}')