tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
for loc, numeros in enumerate(tupla):
    num = int(input('Digite um número de 0 a 20: '))
    
    if num >= 0 and num <= 20:
        break
print(tupla[num])



