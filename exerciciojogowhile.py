from random import randint
num = int(input('Digite um número de 0 a 10: '))
n = randint(1, 11)
cont = 0
while n != num:
    if n > num:
        num = int(input('É maior... Errou, digite outro número: '))
    else:
        num = int(input('É menor... Errou, digite outro número: '))
    cont += 1
print('Você ganhou com {} palpites, pois o número pensado foi: {}'.format(cont, n))