import random
tupla = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))

for c in tupla:
    print(c, end=' ')   
print(f'\n{max(tupla)}')
print(min(tupla))
