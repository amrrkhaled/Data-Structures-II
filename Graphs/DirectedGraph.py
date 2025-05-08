class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []
            return True
        else:
            print(f"Vertex {v} already exists.")
            return False

    def add_edge(self, u, v):
        if u not in self.graph:
            print(f"Vertex {u} does not exist.")
            return False
        if v not in self.graph:
            print(f"Vertex {v} does not exist.")
            return False
        if v in self.graph[u]:
            print(f"Edge from {u} to {v} already exists.")
            return False
        self.graph[u].append(v)
        return True

    def remove_edge(self, u, v):
        if u not in self.graph:
            print(f"Vertex {u} does not exist.")
            return False
        if v not in self.graph:
            print(f"Vertex {v} does not exist.")
            return False
        if v not in self.graph[u]:
            print(f"Edge from {u} to {v} does not exist.")
            return False
        self.graph[u].remove(v)
        return True

    def remove_vertex(self, v):
        if v not in self.graph:
            print(f"Vertex {v} does not exist.")
            return False
        # Remove outgoing edges from v
        del self.graph[v]

        # Remove all incoming edges to v
        for u in self.graph:
            if v in self.graph[u]:
                self.graph[u].remove(v)

        return True

    def get_vertices(self):
        return list(self.graph.keys())

    def get_neighbours(self, v):
        if v not in self.graph:
            print(f"Vertex {v} does not exist.")
            return None
        return self.graph[v]

    def get_indegree(self, v):
        if v not in self.graph:
            print(f"Vertex {v} does not exist.")
            return None
        indegree = 0
        for u in self.graph:
            if v in self.graph[u]:
                indegree += 1
        return indegree

    def get_outdegree(self, v):
        if v not in self.graph:
            print(f"Vertex {v} does not exist.")
            return None
        return len(self.graph[v])
    def get_edges(self):
        edges = []
        for v in self.graph:
            for e in self.graph[v]:
                edges.append((v, e))
        return edges
    
    def is_cyclic(self):
        visited = {vertex: 0 for vertex in self.graph}  # 0 = UNVISITED, 1 = VISITING, 2 = VISITED
        
        def dfs(vertex):
            if visited[vertex] == 1:  # If the vertex is in the recursion stack, there's a cycle
                return True
            if visited[vertex] == 2:  # If the vertex is already fully explored, no cycle here
                return False
            
            visited[vertex] = 1  # Mark as VISITING
            
            for neighbor in self.graph.get(vertex, []):
                if dfs(neighbor):
                    return True
            
            visited[vertex] = 2  # Mark as VISITED
            return False
        
        # Call DFS for each vertex to handle disconnected graphs
        for vertex in self.graph:
            if visited[vertex] == 0:  # If not visited, start DFS
                if dfs(vertex):
                    return True
        
        return False


    def __str__(self):
        return str(self.graph)

    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")
