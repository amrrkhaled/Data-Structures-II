from Graph import Graph
from queue import Queue

def topological_sort(g: Graph):
    if g.is_cyclic():
        raise ValueError("Graph is cyclic")

    # Indegree dictionary initialization
    indegree = {v: g.get_indegree(v) for v in g.get_vertices()}
    
    # Initialize queue and result list
    q = Queue()
    result = []

    # Start by adding all vertices with indegree of 0
    for v in g.get_vertices():
        if indegree[v] == 0:
            q.put(v)

    # Process the queue
    while not q.empty():
        v = q.get()
        result.append(v)

        for u, _ in g.get_neighbours(v):
            indegree[u] -= 1
            if indegree[u] == 0:
                q.put(u)

    # Check if all vertices are processed
    if len(result) != len(g.get_vertices()):
        remaining_vertices = set(g.get_vertices()) - set(result)
        result.extend(remaining_vertices)
        print(f"Graph is disconnected: Adding remaining vertices {remaining_vertices} to the result.")

    return result
