#n = 4 # int(input())
from ast import Global
from re import T


n = int(input())

L = [[] for i in range(n)]

for i in range(n -1):
    #x = ['1 2', '1 3', '3 4'][i].split()#input().split()
    x = input().split()
    a = int(x[0]) - 1
    b = int(x[1]) - 1
    L[a].append(b)
    L[b].append(a)

pontas = [i for i in range(len(L)) if len(L[i]) == 1]

def bfs(grafo, source):
    dados = [[True,None] for i in grafo] # Historico, Distancia, Pai
    dados[source] = [False, 1]
    query = [source]
    maior = [0,1]
    while query:
        u = query.pop()
        for i in grafo[u]:
            if dados[i][0]:
                dados[i][0] = False
                dados[i][1] = dados[u][1] + 1
                if dados[i][1]  > maior[0]:
                    maior = [dados[i][1],1]
                elif dados[i][1] == maior[0]:
                    maior[1] += 1
                query.append(i)
    return maior

pontasdis = []
for i in range(len(pontas)):
    pontasdis.append(bfs(L,pontas[i]))
#print(pontasdis)
maior = [0,1]
for i in pontasdis:
    if i[0] > maior[0]:
        maior = [i[0],i[1]]
    elif i[0] == maior[0]:
        maior[1] += i[1]

print(maior[0])
print(int(maior[1]/2))

def dfs(grafo):
    global tempo
    tempo = 0
    for vertice in grafo:
        if vertice.cor == "Branco":
            dfs_visita(grafo, vertice)
    
    def dfs_visita(grafo, vertice):
        global tempo
        tempo += 1
        vertice.cor = "Cinza"
        for i in grafo[vertice]:
            if i.cor == "Branco":
                i.pai = vertice
                dfs_visita(grafo, i)
        vertice.cor= "Preto"
        tempo += 1
        vertice.ftempo = tempo

def dfs(grafo):
       global tempo
       tempo = 0
       for vertice in grafo:
           if vertice.cor == "Branco":
               dfs_visita(grafo, vertice)
       
       def dfs_visita(grafo, vertice):
           global tempo
           tempo += 1
           vertice.cor = "Cinza"
           for i in grafo[vertice]:
               if i.cor == "Branco":
                   i.pai = vertice
                   dfs_visita(grafo, i)
           vertice.cor= "Preto"
           tempo += 1
           vertice.ftempo = tempo

 
    
    
        