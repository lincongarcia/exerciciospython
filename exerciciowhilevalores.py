n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
escolha = 0
while escolha != 5:
    escolha = int(input('''Obrigado. Agora digite:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
'''))
    if escolha == 1:
        print('A soma dos números é: {}'.format(n1 + n2))
    elif escolha ==2:
        print('A multiplicação dos números é: {}'.format(n1 * n2))
    elif escolha ==3:
        if n1 > n2:
            print('O número maior é: {}'.format(n1))
        else:
            print('O número maior é: {}'.format(n2))
    elif escolha ==4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
print('Fim')
