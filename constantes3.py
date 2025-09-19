from typing import Final
VALOR_10_DESCONTO: Final = 10

valor1 = int(input('Digite o Valor'))

if valor1 >= VALOR_10_DESCONTO:
    print('Você ganhou um desconto de 10%!')
else:
    print('Compra Finalizada')

VALOR_20_DESCONTO: Final = 20

valor2 = int(input('Digite o valor'))

if valor2 >= VALOR_20_DESCONTO:
    print('Você ganhou um desconto de 20%')
else:
    print('Compra Finalizada')

VALOR_30_DESCONTO: Final = 30
valor3 = int(input('Digite o valor'))

if valor3 >= VALOR_30_DESCONTO:
    print('Você ganhou um desconto de 20%')
else:
    print('Compra Finalizada')
