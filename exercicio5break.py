print ('LOJA')
soma = 0
cont = 0
menor = 0
maiscaro = 0
barato = ''
while True:
    nome_prod = str(input('Nome do Produto: '))
    preco = float(input('Preço: '))
    cont += 1
    soma = soma + preco
    if preco > 1000:
        maiscaro += 1
    if cont ==1:
        menor = preco
        barato = nome_prod
    else: 
        if preco < menor:
            menor = preco 
            barato = nome_prod
    continuar = str(input('Quer continuar? [S/N] ')) .upper()
    if continuar == 'N':
        break
print('FIM DO PROGRAMA')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {maiscaro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custou R${menor:.2f}')

    