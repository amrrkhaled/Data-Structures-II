from Graph import Graph 
from queue import PriorityQueue

def prims_mst(g: Graph, start_vertex):
    if g.directed:
        raise ValueError("Graph is directed")
    vertices = g.get_vertices()
    if start_vertex not in vertices:
        print(f"Vertex {start_vertex} does not exist.")
        return None
    
    # Priority Queue to store (weight, vertex, parent)
    pq = PriorityQueue()
    pq.put((0, start_vertex, None))
    
    # Resulting MST graph
    result = Graph()
    
    # Keep track of visited vertices
    visited = set()

    while not pq.empty():
        weight, vertex, parent = pq.get()
        
        if vertex in visited:
            continue
        
        visited.add(vertex)
        result.add_vertex(vertex)
        
        # Add the edge to the MST if the parent is not None
        if parent is not None:
            result.add_edge(parent, vertex, weight)

        # Process neighbors
        for neighbor, edge_weight in g.get_neighbours(vertex):
            if neighbor not in visited:
                pq.put((edge_weight, neighbor, vertex))

    return result

def prims(g: Graph, start_vertex=None):
    if g.directed:
        raise ValueError("Graph is directed")
    if start_vertex is None:
        vertices=g.get_vertices()
        start_vertex=vertices[0]

    mst = prims_mst(g, start_vertex)
    if len(mst.get_vertices()) != len(g.get_vertices()):
        raise ValueError("Graph is disconnected.")

    if mst:
        cost = mst.calculate_cost()
        print(f"Minimum Spanning Tree Cost: {cost}")
        print("Minimum Spanning Tree Edges:")
        mst.print_undirected_graph()

    else:
        print("MST could not be generated.")

