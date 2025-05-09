class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []
            return True
        else:
            print(f"Vertex {v} already exists.")
            return False

    def add_edge(self, u, v, weight=1):
        if u not in self.graph:
            print(f"Vertex {u} does not exist.")
            return False
        if v not in self.graph:
            print(f"Vertex {v} does not exist.")
            return False
        if any(neigh == v for neigh, _ in self.graph[u]):
            print(f"Edge from {u} to {v} already exists.")
            return False

        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))
        return True

    def remove_edge(self, u, v):
        if u not in self.graph or v not in self.graph:
            print(f"One or both vertices do not exist.")
            return False

        # Remove edge from u to v
        found = False
        for i, (neigh, _) in enumerate(self.graph[u]):
            if neigh == v:
                del self.graph[u][i]
                found = True
                break

        if not found:
            print(f"Edge from {u} to {v} does not exist.")
            return False

        # Remove edge from v to u if undirected
        if not self.directed:
            self.graph[v] = [(neigh, w) for neigh, w in self.graph[v] if neigh != u]

        return True

    def remove_vertex(self, v):
        if v not in self.graph:
            print(f"Vertex {v} does not exist.")
            return False

        # Remove all outgoing edges from vertex v
        del self.graph[v]

        # Remove all incoming edges to vertex v
        for u in self.graph:
            self.graph[u] = [
                (neigh, weight) for neigh, weight in self.graph[u] if neigh != v
            ]

        return True


    def get_weight(self, u, v):
        if u not in self.graph:
            print(f"Vertex {u} does not exist.")
            return None
        if v not in self.graph:
            print(f"Vertex {v} does not exist.")
            return None
        for neigh, weight in self.graph[u]:
            if neigh == v:
                return weight
        print(f"No edge from {u} to {v}.")
        return None

    def get_vertices(self):
        return list(self.graph.keys())

    def get_neighbours(self, v):
        if v not in self.graph:
            print(f"Vertex {v} does not exist.")
            return None
        return self.graph[v]

    def get_indegree(self, v):
        if not self.directed:
            raise ValueError("Indegree is only defined for directed graphs.")
        if v not in self.graph:
            print(f"Vertex {v} does not exist.")
            return None
        indegree = 0
        for u in self.graph:
            for neigh, _ in self.graph[u]:
                if neigh == v:
                    indegree += 1
        return indegree

    def get_outdegree(self, v):
        if not self.directed:
            raise ValueError("Outdegree is only defined for directed graphs.")
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
            if visited[vertex] == 1:
                return True
            if visited[vertex] == 2:
                return False

            visited[vertex] = 1

            for neighbor, _ in self.graph.get(vertex, []):
                if dfs(neighbor):
                    return True

            visited[vertex] = 2
            return False

        for vertex in self.graph:
            if visited[vertex] == 0:
                if dfs(vertex):
                    return True

        return False

    def __str__(self):
        return str(self.graph)

    def print_graph(self):
        for v in self.graph:
            neighbors = ', '.join([f"{n}(w={w})" for (n, w) in self.graph[v]])
            print(f"{v} -> {neighbors}")

    def print_undirected_graph(self):

        visited = set()
        for vertex in self.graph:
            for neighbor, weight in self.graph[vertex]:
                # Avoid printing duplicate edges
                if (vertex, neighbor) not in visited and (neighbor, vertex) not in visited:
                    print(f"{vertex} <-> {neighbor}  (w = {weight})")
                    visited.add((vertex, neighbor))
                    visited.add((neighbor, vertex))

    def calculate_cost(self):
        total_cost = 0
        visited = set()

        for vertex in self.graph:
            for neighbor, weight in self.graph[vertex]:
                # Avoid double counting the edge
                if (vertex, neighbor) not in visited and (neighbor, vertex) not in visited:
                    total_cost += weight
                    visited.add((vertex, neighbor))
                    visited.add((neighbor, vertex))

        return total_cost