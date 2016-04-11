from collections import deque



def checkBipartite(graph,root=0):
	#Returns true if a graph is bipartite
	#Defaults to start on root 0, but can be started on any node

	#The Color Array will store the colors of each vertex 
	#True = Purple
	#False = Green
	#None = Unpainted
	colors = [-1 for i in range(0,len(graph))]
	queue = deque()

	if not graph:
		print "Error: Null Graph"
		return False

	if root > len(graph[0]) or root < 0:
		print "Error: Select Valid Root"
		return False

	colors[root] = 1
	queue.append(root)

	#Perform Breadth First Search and mark nodes of the graph the proper color
	while len(queue) != 0:
		node = queue.popleft()

		for child in range(0,len(graph)):
			if graph[node][child]:
				if colors[node] > 0:
					colors[child] = 1 - colors[node]
					queue.append(child)
			#An edge exists but already connects to same color
			elif graph[node][child] and colors[node] == colors[child]:
				return False

	#Reached end without one edge connecting two verticies of the same color
	return True 




if __name__ == "__main__":

	#Matrix Representation of graph
	# Bipartitie
	graph9 = [[0,1,0],\
			 [1,0,1],\
			 [0,1,0]]
	# Not Bipartitie
	graph8 = [[1,1,1],\
			 [1,1,0],\
			 [1,0,1]]
	# Not Bipartitie
	graph7 = [[0,1,0],\
			  [1,0,1],\
			  [0,1,1]]
	# Bipartitie
	graph6 = [[0,0,0],\
			  [1,0,1],\
			  [0,0,0]]
	# Bipartitie
	graph5 = [[0,1,0],\
			  [1,1,1],\
			  [0,1,0]]
	# Bipartitie
	graph4 = [[0,1,0,1],\
			  [1,0,1,1],\
			  [0,1,0,1],\
			  [1,0,1,0]]
	# Bipartitie
	graph3 = [[0,1,0,1,0],\
			  [1,0,1,0,0],\
			  [0,1,0,1,0],\
			  [1,0,1,0,1],\
			  [0,1,0,1,0]]
	# Bipartitie
	graph2 = [[0,1,0,1,0],\
			  [1,0,1,0,1],\
			  [0,1,0,1,0],\
			  [1,1,1,0,1],\
			  [0,1,0,1,0]]

	#Diagnol Relation - Bipartite
	graph1 = [[1,0,0,0,0,0,0,0],\
			  [0,1,0,0,0,0,0,0],\
			  [0,0,1,0,0,0,0,0],\
			  [0,0,0,1,0,0,0,0],\
			  [0,0,0,0,1,0,0,0],\
			  [0,0,0,0,0,1,0,0],\
			  [0,0,0,0,0,0,1,0],\
			  [0,0,0,0,0,0,0,1]]
	#Null Graph
	graph0 = [] 

	if checkBipartite(graph7):
		print "This Graph is bipartite"
	else:
		print "This Graph is not bipartite"