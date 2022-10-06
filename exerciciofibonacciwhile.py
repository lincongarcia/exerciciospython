termo = int(input('quantos termos da fibonacci você deseja mostrar? '))
termo1 = 0
termo2 = 1
print('{} - {}'.format(termo1, termo2), end=' ')
cont = 3
while cont <= termo:
    fb = termo1 + termo2
    print('- {}'.format(fb), end=' ')
    termo1 = termo2
    termo2 = fb
    cont = cont + 1
    
