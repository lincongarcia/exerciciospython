from datetime import date
atual = date.today().year
contmenor = 0
contmaior = 0

for c in range (1, 8):
    nasc = int(input('Qual a data de nascimento da {}ª pessoa? '.format(c)))
    idade = atual - nasc
    if idade >= 18:
        contmaior += 1
    else:
        contmenor += 1
print('No total temos {} pessoas maiores de idade e {} menores de idade.'.format(contmaior, contmenor))
