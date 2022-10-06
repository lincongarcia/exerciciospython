sexo = str(input('Digite seu sexo [M] ou [F]: ')) .upper().strip()

while sexo != 'F' and sexo != 'M':
    sexo = str(input('Dados invalidos por favor informe seu sexo: ')) .upper().strip()
print('sexo {} registrado com sucesso! '.format(sexo))