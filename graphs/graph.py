class graph(object):
	"""
	Graph class - made of nodes and edges

	methods: add_edge, add_edges, add_node, add_nodes, has_node,
	has_edge, nodes, edges, neighbors, del_node, del_edge, node_order,
	set_edge_weight, get_edge_weight
	"""

	DEFAULT_WEIGHT = 1
	DIRECTED = False

	def __init__(self):
		self.node_neighbors = {}

	def __str__(self):
		return "Undirected Graph \nNodes: %s \nEdges: %s" & (self.nodes(), self.edges())

	def add_nodes(self, nodes):
		"""
		Takes a list of nodes as input and adds these to a graph
		"""
		if node not in self.node_neighbors:
			self.node_neighbors[node] = {}
		else:
			raise Exception("Node %s is already in graph" % node)

		