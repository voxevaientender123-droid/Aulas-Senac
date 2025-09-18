# Digite 3 Números
n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
n3 = int(input('Digite um número:'))

# Definição maior/menor

maior = n1
if n2 > maior:
  maior = n2
if n3 > maior:
  maior = n3

menor = n1
if n2 < menor:
  menor = n2
if n3 < menor:
  menor = n3

# Fim da definição

# Definição da Média

media = (n1+n2+n3)/3

# Exibir no Console

print('\n Resultado:')

print('\n Numero maior:', maior)

print('\n Numero menor:', menor)

print('\n Media:', media)

# Fim da Exibição