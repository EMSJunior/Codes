n = int(input())
m = int(input())
s = int(input())

q =0
for i in range(m,n,-1):
    aux=0
    for j in str(i):
        aux = aux + int (j)
    if aux == s:
        q = q + 1
        print(i)
        break
if q == 0:
    print(-1)