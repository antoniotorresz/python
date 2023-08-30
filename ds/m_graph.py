
class Node:
    def __init__(self, data):
        self.data = data
    def get_data(self):
        return self.data
    def __str__(self):
        return self.get_data()
    
class Edge:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
    
    def __str__(self):
        return f'{self.dst} ---> {self.src}'
    
class DirectedGraph:
    def __init__(self):
        self.graph_dict = {}

    def add_node(self, node):
        if not node in self.graph_dict:
            self.graph_dict.update({
                node: []
            })
    
    def connect_nodes(self, edge):
        node1 = edge.src
        node2 = edge.dst
        import pdb; pdb.set_trace()
        if not node1 in self.graph_dict or not node2 in self.graph_dict:
            raise ValueError(f'Either {node1.data} or {node2.data} does not exist in the graph')
        self.graph_dict[node1].append(node2)

    def get_neighbours(self, node):
        return self.graph_dict[node] if node in self.graph_dict else None
    
    def __str__(self):
        line = ''
        for v in self.graph_dict:
            for n in self.graph_dict[v]:
                line += f'{n.src} ---> {n.dst}'


g = DirectedGraph()
g.add_node(Node('s'))
g.add_node(Node('a'))
g.add_node(Node('b'))
g.add_node(Node('c'))

g.connect_nodes(Edge('a', 'b'))
g.connect_nodes(Edge('a', 's'))
g.connect_nodes(Edge('c', 'b'))

print(g)