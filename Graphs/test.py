from Graph import Graph
from topological_sort import topological_sort
from prims import prims

# Test 1: A cyclic graph
g1 = Graph(directed=True)
vertices=['A','B','C','D']
g1.add_vertex(vertices)

g1.add_edge("A", "B")
g1.add_edge("B", "C")
g1.add_edge("C", "A")  # Adding cycle
g1.add_edge("D","A")

# Print the graph structure
print("\nGraph 1 (Cyclic):")
g1.print_graph()

# Topological Sort Test 1
print("\nTopological Sort for Graph 1:")
try:
    sorted_nodes = topological_sort(g1)
    print("Sorted Nodes:", sorted_nodes)
except ValueError as e:
    print(e)


# Test 2: A disconnected graph with multiple components
g2 = Graph(directed=True)
g2.add_vertex(vertices)
g2.add_vertex("E")
g2.add_vertex("F")
g2.add_edge("A", "B")
g2.add_edge("B", "C")
g2.add_edge("D", "E")
g2.add_edge("E", "F")

# Print the graph structure
print("\nGraph 2 (Disconnected):")
g2.print_graph()

# Topological Sort Test 2
print("\nTopological Sort for Graph 2:")
try:
    sorted_nodes = topological_sort(g2)
    print("Sorted Nodes:", sorted_nodes)  # Should correctly sort both components
except ValueError as e:
    print(e)

# Prims Algorithm Test
print("\nPrim's Algorithm on Graph 3:")
g3 = Graph(directed=False)
g3.add_vertex(vertices)
g3.add_vertex("E")
g3.add_vertex("F")
g3.add_vertex("G")

g3.add_edge('G', 'D', 2)
g3.add_edge('G', 'A', 8)
g3.add_edge('D', 'A', 4)
g3.add_edge('D', 'C', 1)
g3.add_edge('D', 'E', 10)
g3.add_edge('D', 'B', 2)
g3.add_edge('A', 'C', 5)
g3.add_edge('C', 'B', 2)
g3.add_edge('B', 'E', 5)
g3.add_edge('A', 'F', 1)
g3.add_edge('C', 'F', 4)
g3.add_edge('B', 'F', 7)


start_vertex = "A"
try:
    prims(g3, start_vertex)
except ValueError as e:
    print(e)



