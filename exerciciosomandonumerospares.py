soma = 0
cont = 0

for c in range (1, 7):
    num = int(input('digite um numero: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('voce informou {} numeros pares e a soma foi {}'.format(cont, soma))