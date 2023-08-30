# Definir el grafo como un diccionario de diccionarios, donde los valores son tuplas (nodo_destino, costo)
graph = {
    's': [('a', 2), ('b', 1), ('c', 3)],
    'a': [('s', 2), ('b', 4), ('g', 7)],
    'b': [('s', 1), ('a', 4), ('c', 5)],
    'c': [('s', 3), ('b', 5), ('d', 2), ('f', 6), ('i', 8)],
    'd': [('s', 6), ('c', 2), ('e', 3), ('f', 2)],
    'e': [('d', 3), ('x', 4)],
    'f': [('c', 6), ('d', 2), ('i', 9)],
    'g': [('a', 7)],
    'i': [('c', 8), ('f', 9)],
    'x': [('e', 4)]
}

def depth_first_search(graph, src, dst, path=[], cost=0):
    path.append(src)
    if src == dst:
        return path, cost
    min_cost_path = None
    for v, c in graph[src]:
        if v not in path:
            new_path, new_cost = depth_first_search(graph, v, dst, path.copy(), cost + c)
            if new_path is not None:
                if min_cost_path is None or new_cost < min_cost_path[1]:
                    min_cost_path = (new_path, new_cost)
    return min_cost_path

def breath_first_search(graph, src, dst):
    queue = [(src, [src], 0)]
    while queue:
        current, path, cost = queue.pop(0)
        if current == dst:
            return path, cost
        for next_vertex, next_cost in graph[current]:
            if next_vertex not in path:
                new_path = path + [next_vertex]
                new_cost = cost + next_cost
                queue.append((next_vertex, new_path, new_cost))

source = 's'
destination = 'x'
dfs_path, dfs_cost = depth_first_search(graph, source, destination)
bfs_path, bfs_cost = breath_first_search(graph, source, destination)

#print(f"The way to go from {source} to {destination} using DFS is {dfs_path} with cost {dfs_cost}")
print(f"The way to go from {source} to {destination} using BFS is {bfs_path} with cost {bfs_cost}")