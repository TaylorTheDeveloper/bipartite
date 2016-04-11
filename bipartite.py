from collections import deque



def checkBipartite(graph,root=0):
	#Returns true if a graph is bipartite
	#Defaults to start on root 0, but can be started on any node

	#The Color Array will store the colors of each vertex 
	#True = Purple
	#False = Green
	#None = Unpainted
	colors = [None for i in range(0,len(graph))]
	queue = deque()

	if not graph:
		print "Error: Null Graph"
		return False

	if root > len(graph[0]) or root < 0:
		print "Error: Select Valid Root"
		return False

	colors[root] = True
	queue.append(root)

	#Perform Breadth First Search and mark nodes of the graph the proper color
	while len(queue) != 0:
		node = queue.popleft()

		for child in range(0,len(graph)):
			if graph[node][child] == 1 and colors[node] == True:
				print "p",node





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