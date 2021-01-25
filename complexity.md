# Calcul de complexité

### Double 

```python
def double_coloration_optimal(G):
	uncolored=G.nodes.copy()	# V
	uncolored_neighbors=[]		# 1
	neighbors=all_neighbors(G) 	# 4*E+1
	while len(uncolored)!=0: 	# 2*V
		#print(uncolored,uncolored_neighbors)
		if len(uncolored_neighbors)==0: # 2+1
			node=uncolored[0]
		else:
			node=uncolored_neighbors[0]
            
		#print("node",node)
		node_neighbors=neighbors[node]  # 1
		node_neighbors_color=[]			# 1
		for neighbor in node_neighbors: # Worst case is Run for (V-1)
			if neighbor in G.color_map: # 2+1
				node_neighbors_color.append(G.color_map[neighbor])
			else:
				uncolored_neighbors.append(neighbor)
         
		uncolored_neighbors=list(set(uncolored_neighbors)) 		# 3
		node_neighbors_color=list(set(node_neighbors_color)) 	# 3
		#print(node_neighbors,node_neighbors_color)
		if len(node_neighbors_color)>=2:	# 2
			#print("node",node,"had too much colors touching it",node_neighbors_color)
			return False					# 1
		else:
			G.setnode_color(node,[x for x in G.two_color if x not in node_neighbors_color][0]) 		# 5
			#print("Colored",node,"in",[x for x in G.two_color if x not in node_neighbors_color][0])
		uncolored.remove(node)	# (V-1)
		if node in uncolored_neighbors: # (V-1)
			uncolored_neighbors.remove(node) #(V-1)
	return True # 1



def neighbors(self,node): #4*E+1
    neighbors=[]
    for edge in self.edges: # run E times
        if node in edge:	
            new_neighbor=list(edge)
            new_neighbor.remove(node)
            neighbors+=new_neighbor
            return neighbors
```

* La complexité en temps est de au pire 2+25\*V+8V²+4*E, donnant une complexité de O(V²+E) dans le pire des cas, et en moyenne O(V+E)





```python
def triple_coloration_optimisation(G,uncolored=None,uncolored_neighbors=None,neighbors=None):
	if uncolored==None: 			# 1 (Happens 1 time)
		uncolored=G.nodes.copy() 	# V
		uncolored_neighbors=[] 		# 1
		neighbors=all_neighbors(G) 	# E

	if len(uncolored)==0: 			# 2
		return True					# 1
	if len(uncolored_neighbors)==0:	# 2
		node=uncolored[0]			# 1
	else:
		node=uncolored_neighbors[0]	# 1
	node_neighbors=neighbors[node] 	# 1
	node_neighbors_color=[]			# 1

	for neighbor in node_neighbors:	# (V-1)
		if neighbor in G.color_map: # 3
			node_neighbors_color.append(G.color_map[neighbor]) 	# 1
		else:
			uncolored_neighbors.append(neighbor)				# 1
	uncolored_neighbors=list(set(uncolored_neighbors))			# 3
	node_neighbors_color=list(set(node_neighbors_color))		# 3
	
	if len(node_neighbors_color)>=3:	# 2		
		return False					# 1
	elif len(node_neighbors_color)==1:	# 2
		H=G._copy()						# V
		G.setnode_color(node,[x for x in G.three_color if x not in node_neighbors_color][0]) 		# 7
		H.setnode_color(node,[x for x in G.three_color if x not in node_neighbors_color][1])		# 7
		uncolored.remove(node)																		# (V-1)
		if node in uncolored_neighbors:																# (V-1)
			uncolored_neighbors.remove(node) 														# 1
		return triple_coloration_optimisation(G,copy.deepcopy(uncolored),copy.deepcopy(uncolored_neighbors),neighbors) or triple_coloration_optimisation(H,copy.deepcopy(uncolored),copy.deepcopy(uncolored_neighbors),neighbors) #2*V times with last occurence complexity = O(V)
	else:
		G.setnode_color(node,[x for x in G.three_color if x not in node_neighbors_color][0])		# 7
		uncolored.remove(node)																		# (V-1)
		if node in uncolored_neighbors:																# (V-1)
			uncolored_neighbors.remove(node)														# (V-1)
		return triple_coloration_optimisation(G,uncolored,uncolored_neighbors,neighbors)			# V times
```

La complexité calculée est donc de V*2^V+E+O(V)