import random
print ('VAMOS JOGAR PAR OU IMPAR')
cont = 0
while True:
    n = int(input('Digite um número: '))
    choice = str(input('Par ou ímpar: [P / I]: ')) .upper() .strip()
    pcchoice = random.randint(0, 50)
    soma = n + pcchoice
    print(f'Você jogou {n} e o computador {pcchoice}. Total deu {soma}')
    if soma % 2 == 0 and choice == 'P':
        print('Deu PAR, você VENCEU!!!')
    elif soma % 2 == 1 and choice == 'I':
        print('Deu ÍMPAR, você VENCEU!!')
    elif soma % 2 == 0 and choice == 'I':
        print('Deu PAR, você PERDEU!!!')
        break
    elif soma % 2 == 1 and choice == 'P':
        print('Deu Ímpar, você PERDEU!!!')
        break
    cont += 1
print(f'Game Over! Você venceu: {cont} vezes.')
    
        







