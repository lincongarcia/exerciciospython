lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado') 
    cont = str(input('Deseja continuar? [S/N] '))
    if cont in 'Nn':
        break
lista.sort()
print(f'Você digitou os valores: {lista}')
