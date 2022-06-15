lista = []
q = int(input())
for i in range(0,q):
  n = int(input())
  if n == 0:
    del(lista[len(lista)-1])
  else:
    lista.append(n)
r = 0
for i in lista:
  r = r + i
print(r)