tupla = ('Palmeiras', 'Corinthians', 'Athletico-PR', 'Internacional', 'Atlético-MG',
'Fluminense', 'Santos', 'São Paulo', 'Flamengo', 'Botafogo', 'Avaí', 'Bragantino', 'Atlético-GO',
'Goiás', 'Ceará', 'Coritiba', 'América-MG', 'Cuiabá', 'Juventude', 'Fortaleza')

print(f'Lista dos times do Brasileirão: {tupla}')
print(f'Os cinco primeiros são: {tupla[0:6]}')
print(f'Os quatro ultimos são: {tupla[16:21]}')
print(f'Em ordem alfabética: {sorted(tupla)}')
print(f'O Coritiba está na posição {tupla.index("Coritiba")+1}')