N, M = [int(i) for i in input().split()]

baldes = [[int(i)]for i in input().split()]

iteracoes = [list(map(int,input().split())) for i in range(M)]

for i in iteracoes:
    if i[0] == 1:
        baldes[i[2]-1].append(i[1])
        baldes[i[2]-1] = sorted(baldes[i[2]-1])
    else:
        menor = baldes[i[1]-1][0]
        maior = baldes[i[2]-1][-1]
        for j in range(i[1]-1, i[2]):
            if baldes[j][0] < menor:
                menor = baldes[j][0]
                
            if baldes[j][-1] > maior:
                maior = baldes[j][-1]
                
        print(maior-menor)
