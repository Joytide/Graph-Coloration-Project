import networkx as nx 
import matplotlib.pyplot as plt


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

	def show(self):
		for node in self.nodes:
			if node not in self.color_map.keys():
				print("Not all nodes were given a color")
				exit()
		G = nx.Graph()
		G.add_edges_from(self.edges)
		values = [self.color_map.get(node,0) for node in self.nodes]
		print(values)
		print(self.nodes)
		nx.draw(G, cmap=plt.get_cmap('viridis'),node_color=values, with_labels=True, font_color='white')
		plt.show()

	def neighbors(self,node):
		neighbors=[]
		for edge in self.edges:
			if node in edge:
				new_neighbor=list(edge)
				new_neighbor.remove(node)
				neighbors+=new_neighbor
		return neighbors

	def setnode_color(self,node,color):
		self.color_map[node]=color

	def node_is_colored(self,node):
		return node in self.color_map

	def all_colored(self):
		ret=True
		for node in self.nodes:
			ret&=self.node_is_colored(node)
		return ret

	def double_coloration(self):
		uncolored=self.nodes.copy()
		uncolored_neighbors=[]
		while len(uncolored)!=0:
			print(uncolored,uncolored_neighbors)
			input()
			if len(uncolored_neighbors)==0:
				node=uncolored[0]
			else:
				node=uncolored_neighbors[0]
			print("node",node)
			node_neighbors=self.neighbors(node)
			node_neighbors_color=[]

			for neighbor in node_neighbors:
				if neighbor in self.color_map:
					node_neighbors_color.append(self.color_map[neighbor])
				else:
					uncolored_neighbors.append(neighbor)
			uncolored_neighbors=list(set(uncolored_neighbors)) 
			node_neighbors_color=list(set(node_neighbors_color)) #Avoid duplicates
			print(node_neighbors,node_neighbors_color)
			input()
			if len(node_neighbors_color)>=2:
				print("node",node,"had too much colors touching it",node_neighbors_color)
				return False
			elif len(node_neighbors_color)==1:
				self.setnode_color(node,[x for x in self.two_color if x not in node_neighbors_color][0])
				print("Colored",node,"in",[x for x in self.two_color if x not in node_neighbors_color][0])

			else:
				self.setnode_color(node,self.two_color[0])
				print("Colored",node,"in",self.two_color[0])

			uncolored.remove(node)
			if node in uncolored_neighbors:
				uncolored_neighbors.remove(node)

		return True
			


#a=[('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')]
a=[('A', 'B'), ('B', 'C'), ('B', 'D'),('A', 'E'),('A', 'F')]
G=Graph(a)
G.double_coloration()
G.show()


