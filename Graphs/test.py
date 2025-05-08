from Graph import Graph
from topological_sort import topological_sort

# Test 1: A cyclic graph
g1 = Graph(directed=True)
g1.add_vertex("A")
g1.add_vertex("B")
g1.add_vertex("C")
g1.add_edge("A", "B")
g1.add_edge("B", "C")
g1.add_edge("C", "A")  # Adding cycle

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
g2.add_vertex("A")
g2.add_vertex("B")
g2.add_vertex("C")
g2.add_vertex("D")
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
