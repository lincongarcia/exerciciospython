from math import factorial
num = int(input('digite um número: '))
f = factorial(num)
print('o número fatorial de {} é: {}'.format(num, f))

while num > 0:
    print('{}'.format(num), end='')
    print(' x ' if num >1 else ' = ' , end='')
    num = num - 1
print('{}'.format(f))
