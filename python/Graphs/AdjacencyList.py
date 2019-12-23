# adjacency list implementation using dynamic arrays instead of lists
class Graph:
    # edges is an array of weighted connections
    def __init__(self, vertices, edges):
        self.adj_list = {i:[] for i in vertices}

        for i in edges:
            self.adj_list[i[0]].append((i[1],i[2]))
            self.adj_list[i[1]].append((i[0],i[2]))
    
    def insert_vertex(self,vertex_value):
        if(vertex_value in self.adj_list):
            return False
        else:
            self.adj_list[vertex_value] = []
            return True

    def insert_edge(self,edge):
        self.adj_list[edge[0]].append((edge[1],edge[2]))
        self.adj_list[edge[1]].append((edge[0],edge[2]))
