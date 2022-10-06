print('BANCO ITAU VTNC')
valor = int(input('Qual valor você deseja sacar? '))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total = total - ced
        totalced += 1
    else:
        print(f'Total de {totalced} cedulas de {ced}')
        if ced ==50:
            ced = 20
        elif ced ==20:
            ced = 10
        elif ced ==10:
            ced = 1
        totalced = 0
        if total == 0:
            break



