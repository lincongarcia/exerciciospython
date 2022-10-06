produto = float(input('Valor do produto: '))
print('''Formas de pagamento
[1] a vista dinheiro/cheque 
[2] a vista no cartão
[3] 2x no cartão 
[4] 3x ou mais no cartão''')
opcao = int(input('Qual sua opção? '))

if opcao == 1:
    print('Valor a vista (dinheiro ou cheque): R${:.2f}' .format(produto - produto * 0.10))
elif opcao == 2:
    print('Valor a vista no cartão: R${:.2f}'.format(produto - produto * 0.05))
elif opcao == 3:
    print('Em até 2x no cartão: R${:.2f}' .format(produto))
elif opcao == 4:
    print('3x ou mais no cartão: R${:.2f}'.format(produto + produto * 0.20))
