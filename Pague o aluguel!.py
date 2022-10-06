VTD = int(input())
VM = int(input())
P = 1
while VTD > 0:
    print(f'pagamento: {P}')
    print(f'antes = {VTD}')
    VTD -= VM
    if VTD < 0:
        print(f'depois = 0')
    else:
        print(f'depois = {VTD}')
    print('-'*5)
    P += 1  