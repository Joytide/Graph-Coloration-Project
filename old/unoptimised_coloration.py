import copy

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