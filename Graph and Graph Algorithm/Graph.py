##############################################################################################################################
#      Project:                  Graph implementation (Object Oriented Way)
#      Info:                     Use a vertex class to represent each node in the graph
#                                It works better for one graph. If we have more graph, adjacency list would be better
##############################################################################################################################

class Vertex:
	def __init__(self,key):
		self.key = key
		self.neighbors = {}

	def __str__(self):
		return str(self.key) + ' neighbors are : ' + str([x.key for x in self.neighbors])

	def addNeighbor(self,nbr,weight=0):
		"""
		@param nbr: the vertex to be added
		@param weight: the weight of the edge
		"""
		self.neighbors[nbr] = weight

	def getNeighbors(self):
		"""
		@return: all the vertexs which are neighbors of current vertex
		"""
		return self.neighbors.keys()

	def getKey(self):
		"""
		@return: the key of the current vertex
		"""
		return self.key

	def getWeight(self,nbr):
		"""
		@return: the weight of the edge between the current vertex and nbr
		"""
		return self.neighbors[nbr]


class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0

	def __contains__(self,n):
		return n in self.vertList

	def __iter__(self):
		"""
		vertList.values are objects of Vertex
		"""
		return iter(self.vertList.values())

	def addVertex(self,key):
		"""
		@param key: the key the of vertex to be added
		"""
		self.numVertices += 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex

	def getVertex(self,n):
		"""
		@param n: the key of the vertex
		"""
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None

	def addEdge(self,f,t,cost=0):
		"""
		@param f: the key of the vertex where the edge from
		@param t: the key of the vertex where the edge to
		@param cost: the weight of the edge
		"""
		if f not in self.vertList:
			nv = self.addVertex(f)
		if t not in self.vertList:
			nv = self.addVertex(t)
		self.vertList[f].addNeighbor(self.vertList[t], cost)

	def getVertices(self):
		"""
		@return: all the keys of the vertexs
		"""
		return self.vertList.keys()

##############################################################################################################################

def main():
	graph = Graph()

	for i in range(6):
		graph.addVertex(i)

	graph.addEdge(0,1,5)
	graph.addEdge(0,5,2)
	graph.addEdge(1,2,4)
	graph.addEdge(2,3,9)
	graph.addEdge(3,4,7)
	graph.addEdge(3,5,3)
	graph.addEdge(4,0,1)
	graph.addEdge(5,4,8)
	graph.addEdge(5,2,1)

	print graph.getVertices()
	
	vertex = graph.getVertex(0)

	print vertex
	print vertex.getNeighbors()

if __name__ == '__main__':
	main()