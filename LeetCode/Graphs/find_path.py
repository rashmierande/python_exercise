graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}


def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph[start]:
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None

print("All paths ",find_path(graph, 'A', 'D'))


def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not graph[start]:
            return []

        all_paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    all_paths.append(newpath)
        return all_paths

print(find_all_paths(graph, 'A', 'D'))


def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph[start]:
            return None

        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

print("Shortest path ",find_shortest_path(graph, 'A', 'D'))


def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges

print("edges ",generate_edges(graph))


def find_isolated_nodes(graph):
    """ returns a list of isolated nodes. """
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated += node
    return isolated

print(find_isolated_nodes(graph))


def cycle_exists(graph):                      # - G is an undirected graph.
    marked = { nodes : False for nodes in graph }     # - All nodes are initially unmarked.
    found_cycle = [False]                 # - Define found_cycle as a list so we can change
                                          # its value per reference, see:
                                          # http://stackoverflow.com/questions/11222440/python-variable-reference-assignment

    for nodes in graph:                           # - Visit all nodes.
        if not marked[nodes]:
            dfs_visit(graph, nodes, found_cycle, nodes, marked)     # - u is its own predecessor initially
        if found_cycle[0]:
            break
    return found_cycle[0]


def dfs_visit(graph, nodes, found_cycle, pred_node, marked):
    if found_cycle[0]:                                # - Stop dfs if cycle is found.
        return
    marked[nodes] = True                                  # - Mark node.
    for v in graph[nodes]:                               # - Check neighbors, where G[u] is the adjacency list of u.
        if marked[v] and v != pred_node:              # - If neighbor is marked and not predecessor,
            found_cycle[0] = True                     # then a cycle exists.
            return
        if not marked[v]:                             # - Call dfs_visit recursively.
            dfs_visit(graph, v, found_cycle, nodes, marked)



graph_example = { 0 : [1],
                  1 : [0, 2, 3, 5],    # edit: corrected from [0, 2] to [0, 2, 3, 5]
                  2 : [1],
                  3 : [1, 4],
                  4 : [3, 5],
                  5 : [1, 4] }

print("cycle exists",cycle_exists(graph_example))
print("cycle exists",cycle_exists(graph))

# check if cycle
# Degree of vertex
# is connected
#
