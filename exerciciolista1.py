lista = []
menor = 0
maior = 0
for c in range(0,5):
    lista.append(int(input(f'Digite um número de 0 a 10 na posição {c}: ')))
    if c == 0:
        menor = maior = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {maior} nas posições: ', end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i} ',end='')
print(f'O menor valor digitado foi: {menor} nas posições: ',end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i} ',end='')



