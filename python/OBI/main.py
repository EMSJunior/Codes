alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']

vogais = ['a','e','i','o','u']

consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z']

palavra = 'ter'

indexOfVogais = [0,4,8,14,20]
distancia = []

aux = []
for i in palavra:
  distancia = []
  if(i in consoantes):
    aux.append(i)

    for j in indexOfVogais:
      distancia.append(int(( (float(alfabeto.index(i))-float(j))**2)**(1/2)))

    aux2 = distancia.copy()
    aux2.sort()
    aux.append(vogais[distancia.index(aux2[0])])

    if (alfabeto.index(i) == 23):
      aux.append(i)
    else:
      if(alfabeto[alfabeto.index(i)+1] in consoantes ):
        aux.append(alfabeto[alfabeto.index(i)+1])
      else:
        aux.append(alfabeto[alfabeto.index(i)+2])

  else:
    aux.append(i)

print(aux)