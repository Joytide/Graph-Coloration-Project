#Ex1
def double_coloration(G):
	uncolored=G.nodes.copy()
	uncolored_neighbors=[]
	while len(uncolored)!=0: #run V times
		#print(uncolored,uncolored_neighbors)
		if len(uncolored_neighbors)==0:
			node=uncolored[0]
		else:
			node=uncolored_neighbors[0]
		#print("node",node)
		node_neighbors=G.neighbors(node) # E
		node_neighbors_color=[]
		for neighbor in node_neighbors:
			if neighbor in G.color_map:
				node_neighbors_color.append(G.color_map[neighbor])
			else:
				uncolored_neighbors.append(neighbor)
		uncolored_neighbors=list(set(uncolored_neighbors)) 
		node_neighbors_color=list(set(node_neighbors_color)) #Avoid duplicates
		#print(node_neighbors,node_neighbors_color)
		if len(node_neighbors_color)>=2:
			print("node",node,"had too much colors touching it",node_neighbors_color)
			return False
		else:
			G.setnode_color(node,[x for x in G.two_color if x not in node_neighbors_color][0])
			#print("Colored",node,"in",[x for x in G.two_color if x not in node_neighbors_color][0])
		uncolored.remove(node)
		if node in uncolored_neighbors:
			uncolored_neighbors.remove(node)
	return True




#Ex1.2
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
def triple_coloration(G):
	uncolored=G.nodes.copy()
	uncolored_neighbors=[]
	neighbors=all_neighbors(G)
	while len(uncolored)!=0:
		#print(uncolored,uncolored_neighbors)
		if len(uncolored_neighbors)==0:
			node=uncolored[0]
		else:
			node=uncolored_neighbors[0]
		#print("node",node)
		node_neighbors=node_neighbors=neighbors[node]
		node_neighbors_color=[]

		for neighbor in node_neighbors:
			if neighbor in G.color_map:
				node_neighbors_color.append(G.color_map[neighbor])
			else:
				uncolored_neighbors.append(neighbor)
		uncolored_neighbors=list(set(uncolored_neighbors))
		node_neighbors_color=list(set(node_neighbors_color)) #Avoid duplicates
		#print(node_neighbors,node_neighbors_color)
		if len(node_neighbors_color)>=3:
			print("node",node,"had too much colors touching it",node_neighbors_color)
			return False
		else:
			G.setnode_color(node,[x for x in G.three_color if x not in node_neighbors_color][0])
			#print("Colored",node,"in",[x for x in G.three_color if x not in node_neighbors_color][0])

		uncolored.remove(node)
		if node in uncolored_neighbors:
			uncolored_neighbors.remove(node)
	return True



#Ex3
def check_triple_coloration(G):
	return "Le graphe est bien coloré avec 3 couleurs" if (1<=len(G.get_colors())<=3) and None not in G.get_colors() else "Le graphe n'a pas été coloré avec 3 couleurs"