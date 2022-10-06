cont = homens = mulher = 0
while True:
    print('Cadastre uma pessoa')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str (input('Sexo: [M/F] ')) .upper()
        if idade > 18:
            cont += 1
        if sexo == 'M':
            homens += 1 
        if idade < 20 and sexo == 'F':
            mulher += 1
    continuar =' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')) .upper() .strip()
        if continuar == 'N':
            break
print('FIM DO PROGRAMA')
print(f'Total de pessoas com mais de 18 anos cadastradas: {cont}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulher} mulheres com menos de 20 anos')



