# adjacency matrix implementation of graph

class Graph:
    # vertices start from 0
    def __init__(self,vertices,edges):
        self.adj_matrix = [
            [0 for i in vertices] for j in vertices
        ]
        for i in edges:
            self.adj_matrix[i[0]][i[1]] = i[2]
            self.adj_matrix[i[1]][i[0]] = i[2]

    def insert_vertex(self,vertex):
        self.adj_matrix.append([0 for i in self.adj_matrix[0]+[]])
        for i in range(len(self.adj_matrix)):
            self.adj_matrix[i].append(0)
    
    def insert_edge(self,edge):
        self.adj_matrix[edge[0]][edge[1]] = edge[2]
        self.adj_matrix[edge[1]][edge[0]] = edge[2]

