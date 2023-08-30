# Definir el grafo como un diccionario de listas
graph = {
    's': ['a', 'b', 'c'],
    'a': ['s', 'b', 'g'],
    'b': ['s', 'a', 'c'],
    'c': ['s', 'b', 'd', 'f', 'i'],
    'd': ['s', 'c', 'e', 'f'],
    'e': ['d', 'x'],
    'f': ['c', 'd', 'i'],
    'g': ['a'],
    'i': ['c', 'f'],
    'x': ['e']
}

def depth_first_search(graph, src, dst, path=[]):
    path.append(src)
    if src == dst:
        return path
    for v in graph[src]:
        if v not in path:
            new_path = depth_first_search(graph, v, dst, path.copy())
            if new_path is not None:
                return new_path

def breath_first_search(graph, src, dst):
    queue = [(src, [src])]
    while queue:
        (current, path) = queue.pop(0)
        for next_vertex in graph[current]:
            if next_vertex not in path:
                new_path = path + [next_vertex]
                if next_vertex == dst:
                    return new_path
                else:
                    queue.append((next_vertex, new_path))

source = 's'
destination = 'x'
dfs_path = depth_first_search(graph, source, destination)
bfs_path = breath_first_search(graph, source, destination)

print(f"The way to go from {source} to {destination} using DFS is {[f'{v} ---> ' for v in dfs_path]}")
print(f"The way to go from {source} to {destination} using BFS is {[f'{v} ---> ' for v in bfs_path]}")
