



def checkBipartite(graph,root=0):
	#Returns true if a graph is bipartite
	#Defaults to start on root 0, but can be started on any node
	
	if not graph:
		print "Error: Null Graph"
		return False

	if root > len(graph[0]) or root < 0:
		print "Error: Select Valid Root"
		return False




if __name__ == "__main__":

	#Matrix Representation of graph
	graph = [[1,1,1],\
			 [1,1,1],\
			 [1,1,1]]

	#graph = []

	if checkBipartite(graph):
		print "This Graph is bipartite"
	else:
		print "This Graph is not bipartite"