N = int(input())
M = int(input())

T = [int(input()) for i in range(M)]

suditos = [i for i in range(N+1)]

salto = 0
j = 0
for i in T:
    while(salto+i < len(suditos)):
        salto += i
        suditos[salto] = 0
    suditos = list(set(suditos))
    salto =0
    if len(suditos) > 10000:
        suditos = suditos[0:10000]


suditos.remove(0)

for i in suditos:
    print(i)
    