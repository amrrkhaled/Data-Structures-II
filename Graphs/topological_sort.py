from DirectedGraph import DirectedGraph
from queue import Queue

def topological_sort(g: DirectedGraph):
    if g.is_cyclic():
        raise ValueError("Graph is cyclic")

    indegree = {v: g.get_indegree(v) for v in g.get_vertices()}
    q = Queue()
    result = []

    for v in g.get_vertices():
        if indegree[v] == 0:
            q.put(v)

    while not q.empty():
        v = q.get()
        result.append(v)

        for u in g.get_neighbours(v):
            indegree[u] -= 1
            if indegree[u] == 0:
                q.put(u)

    return result