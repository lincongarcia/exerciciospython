import random
from time import sleep

print(''' JOKENPÔ
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
choice = int(input('Escolha: '))
jokenpo = ('PEDRA', 'PAPEL', 'TESOURA')
escolhadopc = random.choice(jokenpo)
if choice == 1:
    print('Sua escolha foi: PEDRA')
    print('O computador escolheu: {}'.format(escolhadopc))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    if escolhadopc == 'PEDRA':
        print('Empatou')
    elif escolhadopc == 'PAPEL':
        print('Perdeu Playboy')
    else:
        print('Você GANHOU!!!')
if choice == 2:
    print('Sua escolha foi: PAPEL')
    print('O computador escolheu: {}'.format(escolhadopc))
    if escolhadopc == 'PEDRA':
        print('GANHOU!')
    elif escolhadopc == 'PAPEL':
        print('EMPATOU!')
    else:
        print('PERDEU PLAYBOY!!')
if choice == 3:
    print('Sua escolha foi: TESOURA')
    print('O computador escolheu: {}'.format(escolhadopc))
    if escolhadopc == 'PEDRA':
        print('PERDEU PLAYBOY!')
    elif escolhadopc == 'PAPEL':
        print('GANHOU!!!')
    else:
        print('EMPATOU!')





