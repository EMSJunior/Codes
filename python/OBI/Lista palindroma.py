N = int(input())
lista = [int(i) for i in input().split()]

resp = 0
lista2 = lista[::-1]

i=0
while lista != lista2:
        if lista[i] == lista[N-i-1]:
            i += 1
        elif lista[i] > lista[N-i-1]:
            lista[N-i-2] += lista[N-i-1]
            del lista [N-i-1]
            lista2[i+1] += lista2[i]
            del lista2[i]
            N -= 1
            resp += 1
        else:
            lista[i+1] += lista[i]
            del lista [i]
            
            lista2[N-i-2] += lista2[N-i-1]
            del lista2[N-i-1]
            N -= 1
            resp += 1

print(resp)