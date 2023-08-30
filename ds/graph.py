
#this can be modeled as the graph conections
g = {}
g.update({'s': ['a', 'b', 'c']})


class Vertex:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def __str__(self):
        return self.get_name()

class Edge:
    def __init__(self, vertex_src, vertex_dst):
        self.vertex_src = vertex_src
        self.vertex_dst = vertex_dst
    
    def get_vertex_src(self):
        return self.vertex_src
    
    def get_vertex_dst(self):
        return self.vertex_dst
    
    def __str__(self):
        return f'{self.vertex_src.get_name()} ---> {self.vertex_dst.get_name()}'

#creating directed graph
class DirectedGraph():
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex): #could be named as node also node = vertex
        if vertex in self.graph_dict: 
            return "vertex is already present in graph"
        self.graph_dict[vertex] = []

    def add_edge(self, edge): #creating connection between two nodes
        src_vertex = edge.get_vertex_src()
        dst_vertex = edge.get_vertex_dst()
        if src_vertex not in self.graph_dict:
            raise ValueError(f'vertex {src_vertex.get_name()} does not belong to the graph')
        if dst_vertex not in self.graph_dict:
            raise ValueError(f'vertex {dst_vertex.get_name()} does not belong to the graph')
        self.graph_dict[src_vertex].append(dst_vertex)

    def is_vertex_in(self, vertex):
        return vertex in self.graph_dict
    
    def get_vertex(self, vertex_name):
        for v in self.graph_dict:
            if vertex_name == v.get_name():
                return v
        print(f'vertex {vertex_name} is not present in the graph')

    def get_neighbours(self, vertex):
        return self.graph_dict[vertex]
    
    def __str__(self):
        all_edges = ''
        for v in self.graph_dict:
            for n in self.graph_dict[v]:
                all_edges += n.get_name() + ' ----> ' + n.get_name() + '\n'
        return all_edges


class UndirectedGraph(DirectedGraph):
    def add_edge(self, edge):
        DirectedGraph.add_edge(self, edge)
        edge_back = Edge(edge.get_vertex_dst(), edge.get_vertex_src())
        DirectedGraph.add_edge(self, edge_back)

def build_graph(graph):
    l = ['s', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'x']
    g = graph()
    for v in l:
        g.add_vertex(Vertex(v))
    
    g.add_edge(Edge(g.get_vertex('s'), g.get_vertex('a')) )
    g.add_edge(Edge(g.get_vertex('s'), g.get_vertex('b')) )
    g.add_edge(Edge(g.get_vertex('s'), g.get_vertex('c')) )
    g.add_edge(Edge(g.get_vertex('s'), g.get_vertex('d')) )
    g.add_edge(Edge(g.get_vertex('a'), g.get_vertex('b')) )
    g.add_edge(Edge(g.get_vertex('a'), g.get_vertex('g')) )
    g.add_edge(Edge(g.get_vertex('b'), g.get_vertex('c')) )
    g.add_edge(Edge(g.get_vertex('c'), g.get_vertex('d')) )
    g.add_edge(Edge(g.get_vertex('c'), g.get_vertex('f')) )
    g.add_edge(Edge(g.get_vertex('c'), g.get_vertex('i')) )
    g.add_edge(Edge(g.get_vertex('d'), g.get_vertex('e')) )
    g.add_edge(Edge(g.get_vertex('d'), g.get_vertex('f')) )
    g.add_edge(Edge(g.get_vertex('e'), g.get_vertex('x')) )
    g.add_edge(Edge(g.get_vertex('f'), g.get_vertex('i')) )
    return g

def depth_first_search(graph, src, dst, path): #busqueda por profundidad
    path.append(src)
    if src == dst:
        return path
    for v in graph.get_neighbours(src):
        if v not in path:
            new_path = depth_first_search(graph, v, dst, path)
            if new_path is not None:
                return new_path
            
def breath_first_search(graph, src, dst):
    path = [src]
    queue = [path]
    while queue:
        current_path = queue.pop(0)
        if current_path[-1] == dst:
            return current_path
        for next_vertex in graph.get_neighbours(current_path[-1]):
            new_path = current_path + [next_vertex]
            queue.append(new_path)

g = build_graph(UndirectedGraph)
print(g)
source = g.get_vertex('s')
destination = g.get_vertex('x')
dfs_path = depth_first_search(g, source, destination, [])
bfs_path = breath_first_search(g, source, destination)

print(f"the way to go from {source.get_name()} to {destination.get_name()} using DFS is {[f'{v.get_name()} ---> ' for v in dfs_path]}")
print(f"the way to go from {source.get_name()} to {destination.get_name()} usign BFS is {[f'{v.get_name()} ---> ' for v in bfs_path]}")