from typing import Final
IDADE_MINIMA: Final = 18
Idade = int(input('Digite sua idade:'))
if Idade < IDADE_MINIMA:
    print('Você é Menor de Idade!')
elif Idade >= 18 and 70:
    print('Você é Maior de idade!')
else:
    print('Você tem uma Idade Avançada!')
