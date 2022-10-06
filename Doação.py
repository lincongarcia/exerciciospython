N = C = S = 0
N = float(input())
while N != (-1.0):
    S += N
    C += 1
    N = float(input())
print('VC$ {:.2f}'.format(S))
print('R$ {:.2f}'.format(S * float(2.50)))

