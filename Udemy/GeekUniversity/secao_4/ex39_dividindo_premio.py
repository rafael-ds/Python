# Programa que divide um premio de R$780mil para 3 ganhadores
# O primeiro receberá 46%
# O segundo receberá 32%
# O terceiro receberá o restante

premio = float(780.000)
ganhador_1 = (premio * 46) / 100
ganhador_2 = (premio * 32) / 100
ganhador_3 = (premio * 22) / 100

print(f'O primeiro ganhador receberá a quantia de R${ganhador_1}')
print(f'O segundo ganhador receberá a quantia de R${ganhador_2}')
print(f'O terceiro ganhador receberá a quantia de R${ganhador_3}')