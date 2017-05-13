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

	def has_node(self, node):
		"""
		Return boolean to indicate whether a node exists in the graph
		"""
		return node in self.node_neighbors

	def add_edge(self, edge, wt=DEFAULT_WEIGHT, label=""):
		"""
		Add an edge to the graph connecting two nodes.
		An edge, here, is a pair if node like C(m, n) or a tuple
		"""
		u, v = edge
		if (v not in self.node_neighbors[u] and u not in self.node_neighbors[v]):
			self.node_neighbors[u][v] = wt
			if (u!=v):
				self.node_neighbors[v][u] = wt
		else:
			raise Exception("Edge (%s, %s)already added in the graph" % (u, v))

	def add_edges(self, edges):
		""" Added multiple edges in one go. Edges, here, is a list of
		tuples"""
		for edge in edges:
			self.add_edge(edge)

	def nodes(self):
		"""
		Returns a list of nodes in a graph
		"""
		return self.node_neighbors.keys()