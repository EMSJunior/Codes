valor, nilhas, nrotas = [int(i) for i in input().split()]

ilhas = [[] for i in range(nilhas)]
for i in range(nrotas):
    inp = input().split()
    ilhas[int(inp[0])-1].append([int(inp[1])-1, int(inp[2]), int(inp[3])])
    ilhas[int(inp[1])-1].append([int(inp[0])-1, int(inp[2]), int(inp[3])])

inicio, destino = [int(i)-1 for i in input().split()]

atual = inicio
historico = []
tempo = 0
preco = 0
resp = []


p = [0 for i in range(nilhas)]
pback = p.copy()

rotasfeitas = []

while(1):
    print(atual, tempo, preco)
    for i in ilhas:
            print(i)
    if ilhas[atual][p[atual]][0] not in historico:
        print("V" , ilhas[atual][p[atual]])
        tempo += ilhas[atual][p[atual]][1]
        preco += ilhas[atual][p[atual]][2]
        historico.append(atual)
        atual = ilhas[atual][p[historico[-1]]][0]
        
    else:
        print("F" , ilhas[atual][p[atual]])
        ilhas[atual].append(ilhas[atual].pop(0))
        continue
    
    if atual == destino:
        print(atual, tempo, preco)
        if preco <= valor:
            if historico not in rotasfeitas:
                rotasfeitas.append(historico)
                resp.append(tempo)
            else:
                ilhas[historico[-1]].append(ilhas[historico[-1]].pop(0))
                
            
        print(resp , "\n\n_____________\n\n")
        for i in ilhas:
            print(i)
        tempo, preco, atual = [0,0,inicio]
        p = pback.copy()
        historico = []
        
        
    


print(sorted(resp))
