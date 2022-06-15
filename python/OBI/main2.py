aux = []
numeros = input()
for i in range(int(numeros)):
  numero = int(input())
  if numero != 0:
    aux.append(numero)
  else:
    aux.remove(aux[len(aux)-1]) 

print(sum(aux))