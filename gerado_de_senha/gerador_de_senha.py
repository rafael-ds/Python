import string
from random import choice


letra = string.ascii_letters
numeros = string.digits
caracteres = '_@$&'

comcat = letra + numeros + caracteres
temp = []

# Randomização dos elementos
cont = 0
while cont < 8:
    randomizar = choice(comcat)
    temp.append(randomizar)
    cont += 1

# Convertendo a lista temp em string
convecao_str = ''.join(temp)
