class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo  = [[0] * self.vertices] * self.vertices
        print(self.grafo)

    def addAresta(self, u, v):
        self.grafo[u-1][v-1] = 1

    def addArestapeso(self, u, v, p):
        self.grafo[u-1][v-1] = p