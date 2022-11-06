A =int(input())
B =int(input())
soma = A + B

resp = [ -1, -1]
for i in range(1,A+1):
    j = soma / i
    brancos = ( i - 2) * ( j - 2)
    if brancos == B:
        resp[0] = i
        resp[1] = j
        break


print(int(resp[0]), int(resp[1]))