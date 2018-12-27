'''
Chase M. Peak
graph abstract data structure
'''

class Vertex():
    def __init__(self, key):
        self.key = key
        self.adjacent_to = []


class Graph():
    def __init__(self, filename = None):
        self.vertex_list = {}
        self.num_vertices = 0
        self.create_graph(filename)

    def create_graph(self, filename):
        try:
            vertex_file = open(filename, 'r')
        except:
            raise FileNotFoundError
        vertex_pairs = vertex_file.readlines()
        vertex_file.close()

        for i in vertex_pairs:
            i = i.split()
            for j in i:
                self.add_vertex(j)
            self.add_edge(i[0],i[1])

    
    def add_vertex(self, key):
        if not key in self.vertex_list:
            self.num_vertices += 1
            vert = Vertex(key)
            self.vertex_list[key] = Vertex(key)


    def get_vertex(self, key):
        if key in self.vertex_list:
            return self.vertex_list[key]


    def add_edge(self, v1, v2):
        if v1 not in self.vertex_list:
            self.add_vertex(v1)
        if v2 not in self.vertex_list:
            self.add_vertex(v2)
        self.vertex_list[v1].adjacent_to.append(v2)
        self.vertex_list[v2].adjacent_to.append(v1)


    def get_vertices(self):
        return sorted(list(self.vertex_list))
