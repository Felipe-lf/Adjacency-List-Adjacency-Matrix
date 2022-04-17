from mimetypes import init


class graph:
    
    def __init__(self, vert):
        self.vert = vert
        self.graph = [[] for i in range(self.vert)]

    def add_arest(self, u, v):
        self.graph[u-1].append(v)
        self.graph[v-1].append(u)
    def show_list(self):
        for i in range(self.vert):
            print(f'{i+1}:', end='  ')
            for j in self.graph[i]:
                print(f'{j}  ->', end='  ')
            print('')

g = graph(6)

g.add_arest(1,2)
g.add_arest(1,5)
g.add_arest(2,3)
g.add_arest(2,5)
g.add_arest(3,4)
g.add_arest(4,5)
g.add_arest(4,6)

g.show_list()
