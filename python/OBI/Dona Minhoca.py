#n = 4 # int(input())
from time import time


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

def dfs(grafo, source):
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


  
    
        