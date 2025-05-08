from DirectedGraph import DirectedGraph
from topological_sort import topological_sort

g = DirectedGraph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")
g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("C", "A")
g.add_edge("B", "D")
g.print_graph()

print("\nTopological Sort:")
sorted_nodes = topological_sort(g)
for node in sorted_nodes:
    print(node)
# Example Output:

# Output:
# A -> ['B', 'C']
# B -> ['D']
# C -> ['D']
# D -> []
