#Matrizes

# Criação da Matriz 5x5:

Matriz_a = [[ 1 , 2 , 3 , 4, 5],
            [ 7 , 4 , 8 , 4, 1],
            [ 5 , 2 , 4 , 8, 3],
            [ 2 , 9 , 9 , 2, 7],
            [ 6 , 2 , 4 , 1, 9]]

print("Matriz A:")
for i in Matriz_a: # print de Forma organizada
    print(i) # Aqui, i se refere a cada linha, e 'printa' uma de cada vez
    
#Soma de Matrizes por outra

Matriz_b = [[ 8 , 7 , 6 , 5, 4],
            [ 2 , 5 , 1 , 5, 8],
            [ 4 , 7 , 5 , 1, 6],
            [ 7 , 0 , 0 , 7, 2],
            [ 3 , 7 , 5 , 8, 0]]
print("Matriz B: ")
for i in Matriz_b:
    print(i)

# Aqui somamos os vares de mesmo indice e adiocionanmos na Matriz C



# Matriz C[0][0] = Matriz_a[0][0] + Matriz_b[0][0] ...

# Usamos um for para somar todos de uma linha
# E usamos outro for para cada linha
# OBS: Tamanho das Matrizes tem que ser igual

Matriz_c = [[None for i in Matriz_a[0]] for i in Matriz_a]  # Criando C com o tamanho de A

print("Matriz C: ")
for i in Matriz_c:
    print(i)

for i in range(len(Matriz_a[0])):
    for j in range(len(Matriz_b)):
        Matriz_c[i][j] = Matriz_a[i][j] + Matriz_b[i][j]
        
print("Matriz C depois da soma: ")
for i in Matriz_c:
    print(i)
    
    
print("Teste de soma: ")
print(Matriz_b + Matriz_a, end="\n") # Não funcionará

# Multiplicção de Matrizes
# Aqui, é primordial que o numeros de colunas(a) seja igual o número de linhas(b)

# Pois, na multiplicação, pois multiplicamos a linha pela coluna:

# Criarei uma DEF para usar na exponenciação

def multiplicarMatriz(MA, MB):
    MatrizReturn = [[0 for i in MA] for i in MB]
    for k in range(len(MA)):
        for j in range(len(MB[0])):
            for i in range(len(MB)):
                MatrizReturn[k][j] += MA[k][i]* MB[i][j]                
    return MatrizReturn

MatrizMultiplicada = multiplicarMatriz(Matriz_a, Matriz_b)
print("Matriz A * Matriz B:")
for i in MatrizMultiplicada:
    print(i)
        
# Exponenciação 
# Só possivel em matriz quadrada

# Vamos multiplicar a Matriz por ela mesma n vezes

def ElevarMatriz(Matriz, n):
    for i in range(n):
        Matriz = multiplicarMatriz(Matriz, Matriz)
    return Matriz

print("Matriz A²:")
MatrizElevada = ElevarMatriz(Matriz_a, 2)
for i in MatrizElevada:
    print(i)