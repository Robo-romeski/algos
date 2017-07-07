from graph import graph
from copy import deepcopy

class digraph(graph):
	"""
	Directed Graph class - made of nodes and edges

	methods: add_edge, add_edges, add_node, add_nodes, has_node,
	has_edge, nodes, edges, neighbors, del_node, del_edge, node_order,
	set_edge_weight, get_edge_weight, 

	"""
	def __init__(self):
		self.node_neighbors = {}
