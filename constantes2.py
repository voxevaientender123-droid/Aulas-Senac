from typing import Final
VALOR_MINIMO_DESCONTO: Final = 100

valor = float(input('Digite o Valor: ')) 



DESCONTO: Final = 0.1 #desconto de 10%
calcular_desconto = valor * DESCONTO
valor_final = valor - calcular_desconto


if valor >= VALOR_MINIMO_DESCONTO:
    print('Você ganhou um desconto de 10%! valor a pagar com desconto sera :', valor_final )
else:
    print('Compra Finalizada')