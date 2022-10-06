termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
cont = 1
total = 0
more = 10
while more != 0:
    total = total + more
    while cont <= total:
        print(termo, end=' ')
        termo += razao
        cont += 1
    print('Pausa')
    more = int(input('Quantos termos você quer mostrar a mais? '))
print('Fim')
