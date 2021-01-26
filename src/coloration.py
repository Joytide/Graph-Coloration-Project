import copy

#Ex1
def all_neighbors(G): #O(E)
	neighbors={}
	for (node1,node2) in G.edges: # run E times
		if node1 in neighbors:
			neighbors[node1].append(node2)
		else:
			neighbors[node1]=[node2]

		if node2 in neighbors:
			neighbors[node2].append(node1)
		else:
			neighbors[node2]=[node1]

	return neighbors

def double_coloration_optimal(G):
	uncolored=G.nodes.copy()
	uncolored_neighbors=[]
	neighbors=all_neighbors(G) #E
	while len(uncolored)!=0: #run V times  O(V)
		print(uncolored,uncolored_neighbors)
		if len(uncolored_neighbors)==0:
			node=uncolored[0]
		else:
			node=uncolored_neighbors[0]
		print("node",node)
		node_neighbors=neighbors[node]
		node_neighbors_color=[]
		for neighbor in node_neighbors:
			if neighbor in G.color_map:
				node_neighbors_color.append(G.color_map[neighbor])
			else:
				uncolored_neighbors.append(neighbor)
		uncolored_neighbors=list(set(uncolored_neighbors)) 
		node_neighbors_color=list(set(node_neighbors_color)) #Avoid duplicates
		print(node_neighbors,node_neighbors_color)
		if len(node_neighbors_color)>=2:
			print("node",node,"had too much colors touching it",node_neighbors_color)
			return False
		else:
			G.setnode_color(node,[x for x in G.two_color if x not in node_neighbors_color][0])
			print("Colored",node,"in",[x for x in G.two_color if x not in node_neighbors_color][0])
		uncolored.remove(node)
		if node in uncolored_neighbors:
			uncolored_neighbors.remove(node)
	return True




#Ex2

def triple_coloration_optimisation(G,uncolored=None,uncolored_neighbors=None,neighbors=None):
	if uncolored==None: #Initialisation
		uncolored=G.nodes.copy()
		uncolored_neighbors=[]
		neighbors=all_neighbors(G)

	if len(uncolored)==0:
		return True
	if len(uncolored_neighbors)==0:
		node=uncolored[0]
	else:
		node=uncolored_neighbors[0]
	node_neighbors=node_neighbors=neighbors[node]
	node_neighbors_color=[]

	for neighbor in node_neighbors:
		if neighbor in G.color_map:
			node_neighbors_color.append(G.color_map[neighbor])
		else:
			uncolored_neighbors.append(neighbor)
	uncolored_neighbors=list(set(uncolored_neighbors))
	node_neighbors_color=list(set(node_neighbors_color))

	if len(node_neighbors_color)>=3:
		return False
	elif len(node_neighbors_color)==1:
		H=G._copy()
		G.setnode_color(node,[x for x in G.three_color if x not in node_neighbors_color][0])
		H.setnode_color(node,[x for x in G.three_color if x not in node_neighbors_color][1])
		uncolored.remove(node)
		if node in uncolored_neighbors:
			uncolored_neighbors.remove(node)
		return triple_coloration_optimisation(G,copy.deepcopy(uncolored),copy.deepcopy(uncolored_neighbors),neighbors) or triple_coloration_optimisation(H,copy.deepcopy(uncolored),copy.deepcopy(uncolored_neighbors),neighbors)
	else:
		G.setnode_color(node,[x for x in G.three_color if x not in node_neighbors_color][0])
		uncolored.remove(node)
		if node in uncolored_neighbors:
			uncolored_neighbors.remove(node)
		return triple_coloration_optimisation(G,uncolored,uncolored_neighbors,neighbors)






#Ex3
def check_triple_coloration(G):
	if not (1<=len(G.get_colors())<=3) or None in G.get_colors() or any(G.color_map(node1)==G.color_map(node2) for (node1,node2) in self.edges):
		return "This graph is not 3-colored"
	else:
		return "This graph is 3-colored"