class graph:
    def __init__(self, vert):
        self.vert = vert
        self.graph = [[0]*self.vert for i in range(self.vert)]
    
    def add_arest(self, u, v):
        self.graph[u-1][v-1] = 1
        self.graph[v-1][u-1] = 1

    def show_matrix(self):
        print("The adjacency matrix is:")
        for i in range(self.vert):
            print(self.graph[i])

g = graph(6)

g.add_arest(1,2)
g.add_arest(1,5)
g.add_arest(2,3)
g.add_arest(2,5)
g.add_arest(3,4)
g.add_arest(4,5)
g.add_arest(4,6)

g.show_matrix()