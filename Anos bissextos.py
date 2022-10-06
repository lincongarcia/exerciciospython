AI = int(input())
AF = int(input())
cont = 0
for x in range(AI , AF + 1):
    if x % 4 == 0 and x % 100 != 0 or x % 400 ==0:
        print(x)
        cont += 1
print (f'bissextos: {cont}')