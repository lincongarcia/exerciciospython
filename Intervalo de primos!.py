
N1 = int(input())
N2 = int(input())
cont = 0
for i in range(N1, N2 + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
            
            

            cont += 1

print(f'primos:', cont)