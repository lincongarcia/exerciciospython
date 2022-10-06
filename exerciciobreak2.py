cont = 1
while True:
    n = int(input('Quer ver a tabuaba de qual valor? '))
    if n < 0:
        break
    while cont <= 10:
        print(f'{n} X {cont} = {n * cont}\n')
        cont += 1
    cont = 1
print(f'PROGRAMA TABUADA ENCERRADO - VOLTE SEMPRE!')
