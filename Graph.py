import copy

class Graph():
	def __init__(self,edges=None):
		if edges:
			self.edges=edges
		else:
			self.edges=[]
		self.color_map={}
		self.nodes=list(set([x for (x,y) in self.edges]+[y for (x,y) in self.edges]))
		self.nodes.sort()
		self.two_color=[0,1]
		self.three_color=[0,0.5,1]

	def show(self,force = False):
		n=0
        
		for node in self.nodes:
			if node not in self.color_map.keys():
				n+=1
				
		if n!=0 and not force:	
 			print("Not displaying graph since "+str(n)+" nodes were not given a color")
 			return False
		import networkx as nx 
		import matplotlib.pyplot as plt
		G = nx.Graph()
		G.add_edges_from(self.edges)
		#self.color_map=dict(sorted(self.color_map.items()))
		#print(self.color_map,self.nodes)
		values = [self.color_map.get(node,0) for node in G.nodes]
		#print(values)
		print(G.nodes,self.nodes,self.color_map)
		nx.draw(G, cmap=plt.get_cmap('viridis'),node_color=values, with_labels=True, font_color='white')
		plt.show()
        
        


	def neighbors(self,node): #4E+1
		neighbors=[]
		for edge in self.edges: # run E times
			if node in edge:	
				new_neighbor=list(edge)
				new_neighbor.remove(node)
				neighbors+=new_neighbor
		return neighbors

	def setnode_color(self,node,color):
		self.color_map[node]=color
    

	def get_colors(self):
		colors=[]
		for node in self.nodes:
			if node not in self.color_map:
				colors.append(None)
			else:
				colors.append(self.color_map[node])
		return list(set(colors))
    
	def _copy(self):
		H=Graph(copy.deepcopy(self.edges))
		H.color_map=copy.deepcopy(self.color_map)
		return H
    

    
    



