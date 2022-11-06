L, C = [int(i) for i in input().split()]
#L, C = [3,5]

P = int(input())
#P = 3

tab = [[0] * C for i in range(L)] # Brancos

resp = 0
pretos = []

for i in range(P):
    x = input().split()
    #x = ['2 2','2 3','3 5'][i].split()
    tab[int(x[0])-1][int(x[1])-1] = -1 # Preto
    pretos.append([(int(x[0])-1),(int(x[1])-1)])

def printl():
    global L,C,tab, pretos;
    
    for i in range(L):
        for j in range(C):
            print(tab[i][j], end=' ')
        print("")
    print(pretos)

for k in pretos:
    i = k[0]
    j = k[1]
    
    # i + 1
    if i+1 >= 0 and i+1 < L:
        if tab[i+1][j] >= 0:
            tab[i+1][j] += 1
        
    # i - 1
    if i-1 >= 0 and i-1 < L:
        if tab[i-1][j] >= 0:
            tab[i-1][j] += 1
    
    # j + 1
    if j+1 >= 0 and j+1 < C:
        if tab[i][j+1] >= 0:
            tab[i][j+1] += 1
        
    # j - 1
    if j-1 >= 0 and j-1 < C:
        if tab[i][j-1] >= 0:
            tab[i][j-1] += 1

for i in range(L):
    for j in range(C):
        if tab[i][j] > 0:
            # i + 1
            if i+1 >= 0 and i+1 < L:
                if tab[i+1][j] > 0:
                    tab[i+1][j] += 1
                
            # i - 1
            if i-1 >= 0 and i-1 < L:
                if tab[i-1][j] > 0:
                    tab[i-1][j] += 1
            
            # j + 1
            if j+1 >= 0 and j+1 < C:
                if tab[i][j+1] > 0:
                    tab[i][j+1] += 1
                
            # j - 1
            if j-1 >= 0 and j-1 < C:
                if tab[i][j-1] > 0:
                    tab[i][j-1] += 1

def tirar(maxn):
    for i in range(L):
        for j in range(C):
            if tab[i][j] > 0 and tab[i][j] < maxn:
                # i + 1
                if i+1 >= 0 and i+1 < L:
                    if tab[i+1][j] > 0:
                        if tab[i][j] > tab[i+1][j]:
                            tab[i][j] = 0
                        else:
                            tab[i+1][j] = 0
                    
                # i - 1
                if i-1 >= 0 and i-1 < L:
                    if tab[i-1][j] > 0:
                        if tab[i][j] > tab[i-1][j]:
                            tab[i][j] = 0
                        else:
                            tab[i-1][j] = 0
                
                # j + 1
                if j+1 >= 0 and j+1 < C:
                    if tab[i][j+1] > 0:
                        if tab[i][j] > tab[i][j+1]:
                            tab[i][j]  = 0
                        else:
                            tab[i][j+1] = 0
                    
                # j - 1
                if j-1 >= 0 and j-1 < C:
                    if tab[i][j-1] > 0:
                        if tab[i][j] > tab[i][j-1]:
                            tab[i][j] = 0 
                        else:
                            tab[i][j-1] = 0

for i in range(1,5):
    tirar(i)

for linha in tab:
    for i in linha:
        if i > 0:
            resp += 1


#printl()

print(resp)