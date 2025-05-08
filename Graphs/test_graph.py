import unittest
from Graph import Graph  

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.directed = Graph(directed=True)
        self.undirected = Graph(directed=False)

    def test_add_vertex(self):
        self.assertTrue(self.directed.add_vertex("A"))
        self.assertFalse(self.directed.add_vertex("A"))  # duplicate

    def test_add_edge_directed(self):
        g = self.directed
        g.add_vertex("A")
        g.add_vertex("B")
        self.assertTrue(g.add_edge("A", "B", 5))
        self.assertFalse(g.add_edge("A", "B"))  # duplicate
        self.assertEqual(g.get_weight("A", "B"), 5)
        self.assertIsNone(g.get_weight("B", "A"))

    def test_add_edge_undirected(self):
        g = self.undirected
        g.add_vertex("A")
        g.add_vertex("B")
        g.add_edge("A", "B", 7)
        self.assertEqual(g.get_weight("A", "B"), 7)
        self.assertEqual(g.get_weight("B", "A"), 7)

    def test_remove_edge_directed(self):
        g = self.directed
        g.add_vertex("A")
        g.add_vertex("B")
        g.add_edge("A", "B")
        self.assertTrue(g.remove_edge("A", "B"))
        self.assertFalse(g.remove_edge("A", "B"))  # already removed

    def test_remove_edge_undirected(self):
        g = self.undirected
        g.add_vertex("A")
        g.add_vertex("B")
        g.add_edge("A", "B")
        g.remove_edge("A", "B")
        self.assertIsNone(g.get_weight("A", "B"))
        self.assertIsNone(g.get_weight("B", "A"))

    def test_remove_vertex(self):
        g = self.undirected
        g.add_vertex("A")
        g.add_vertex("B")
        g.add_edge("A", "B")
        self.assertTrue(g.remove_vertex("A"))
        self.assertFalse(g.remove_vertex("A"))  # already removed
        self.assertIsNone(g.get_weight("B", "A"))

    def test_get_vertices_and_edges(self):
        g = self.directed
        g.add_vertex("X")
        g.add_vertex("Y")
        g.add_edge("X", "Y", 3)
        self.assertEqual(set(g.get_vertices()), {"X", "Y"})
        self.assertIn(("X", ("Y", 3)), g.get_edges())

    def test_get_neighbours(self):
        g = self.directed
        g.add_vertex("M")
        g.add_vertex("N")
        g.add_edge("M", "N", 9)
        self.assertEqual(g.get_neighbours("M"), [("N", 9)])
        self.assertEqual(g.get_neighbours("N"), [])

    def test_indegree_outdegree_directed(self):
        g = self.directed
        g.add_vertex("A")
        g.add_vertex("B")
        g.add_edge("A", "B")
        self.assertEqual(g.get_indegree("B"), 1)
        self.assertEqual(g.get_outdegree("A"), 1)

    def test_indegree_outdegree_undirected(self):
        g = self.undirected
        g.add_vertex("A")
        g.add_vertex("B")
        g.add_edge("A", "B")
        with self.assertRaises(ValueError):
            g.get_indegree("B")
        with self.assertRaises(ValueError):
            g.get_outdegree("A")

    def test_is_cyclic_directed(self):
        g = self.directed
        g.add_vertex("A")
        g.add_vertex("B")
        g.add_vertex("C")
        g.add_edge("A", "B")
        g.add_edge("B", "C")
        g.add_edge("C", "A")
        self.assertTrue(g.is_cyclic())

    def test_is_cyclic_directed_false(self):
        g = self.directed
        g.add_vertex("A")
        g.add_vertex("B")
        g.add_vertex("C")
        g.add_edge("A", "B")
        g.add_edge("B", "C")
        self.assertFalse(g.is_cyclic())

if __name__ == "__main__":
    unittest.main()
