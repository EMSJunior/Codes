from math import floor


n, m = [int(i) for i in input().split()]

fac = 2
for i in range(n,1,-1):
    fac = i + fac
if m > 0:
    print((floor(fac/m)+1)*(floor(3/2)))
else:
    print(fac)