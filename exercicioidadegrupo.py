mediaidade = 0
maisvelho = 0
idademulhermenor = 0
nomevelho = ''
cont = 0
for c in range (1,5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite M para masculino ou F para feminino: ')) .upper()
    mediaidade = mediaidade + idade
    if c == 1 and sexo == 'M':
        maisvelho = idade
        nomevelho = nome
    if sexo == 'M' and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome
    if sexo == 'F':
        idademulhermenor = idade
    else:
        if idademulhermenor < 20:
            cont += 1
print('A média da idade do grupo é: {}'.format(mediaidade /4))
print('A idade do homem mais velho é: {} e o nome dele é: {}'.format(maisvelho, nomevelho))
print('quantas mulheres tem menos de 20 anos: {}'.format(cont))

        
