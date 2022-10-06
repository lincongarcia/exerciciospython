c = ''
cont = 0
somar = 0
maior = 0
menor = 0
while c != 'N': 
    num = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S] ou [N] ')).upper()
    c = continuar
    cont += 1
    somar = somar + num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print('Você digitou {} números e a média foi: {:.2f}'.format(cont, somar/cont))
print('O maior valor foi: {} e o menor foi: {}'.format(maior, menor))




