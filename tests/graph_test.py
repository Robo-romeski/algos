import os, sys
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
import unittest
from graphs.graph import graph

class test_graph(unittest.TestCase):
	def setUp(self):
		self.gr = graph()
		self.gr.add_nodes(["a", "b", "c", "d", "e", "f"])
		self.gr.add_edge(("a","b"))
		self.gr.add_edge(("a","f"))
		self.gr.add_edge(("b","c"))
		self.gr.add_edge(("c","e"))
		self.gr.add_edge(("c","d"))
		self.gr.add_edge(("d","f"))
		