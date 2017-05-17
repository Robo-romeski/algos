from collections import deque
from copy import deepcopy
from union_find.unionfind import UnionFind
import heapq

def BFS(gr, s):
	"""Breath first search
	Returns a list of nodes that are "findable" from s"""
	if not gr.has_node(s):
		raise Exception("Node %s not in graph" % s)
	nodes_explored = set([s])
	q = deque([s])
	while len(q) !=0:
		node = q.popleft()
		for each in gr.neighbors(node):
			if each not in nodes_explored:
				nodes_explored.add(each)
				q.append(each)
	return nodes_explored