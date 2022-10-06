valor = float(input(''))
quantidade = int(input(''))
total = valor * quantidade
desconto = total * 0.10
total_final = total-desconto
print(f'{total:.2f}')

desconto_por_unidade= total * quantidade/100
print (f'{total_final-desconto_por_unidade:.2f}')
