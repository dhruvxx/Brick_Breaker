import numpy as np
from headers import *

class Graph: 
	def __init__(self,vertices):
		self.vertices = v
		self.adj = [[] for i in range(v)]

	def AddEdge(self,v,w):
		self.adj[v].append(w)

	def DFS(self,source):
		visited = [False for i in range(self.v)]
		stack = []
		stack.append(s)
		while(len(stack)):
			s = stack[-1]
			stack.pop()
			if(not visited[s]):
				print(s,end=' ')
				visited[s] = True

			for n in self.adj[s]:
				if(not visited[n]):
					stack.append(n)

	def imploding_bricks(self):
		