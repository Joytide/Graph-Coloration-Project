# Explications et commentaires du code

### Fonction colorant les sommes de deux couleurs double_coloration

```python
def double_coloration(self):
	uncolored=self.nodes.copy() # creation d'une liste regroupant les nodes non-colorés
	uncolored_neighbors=[]    # creation d'une liste regroupant les nodes non-colorés et avec au moins un voisin coloré
	while len(uncolored)!=0:  # parcours de toutes les nodes non coloré(jusqu'à e que la liste soit vide)
		print(uncolored,uncolored_neighbors)
		#input()
		if len(uncolored_neighbors)==0:  
			node=uncolored[0]   # si la liste des nodes non-colorés et avec un voisin coloré est vide on choisit la première node de la liste des nodes non-coloré
		else:
			node=uncolored_neighbors[0] # si la liste des nodes non-colorés et avec un voisin coloré n'est pas vide on choisit sa première node
		print("node",node)
		node_neighbors=self.neighbors(node)  # crée un tableau avec les voisins de la node
		node_neighbors_color=[]  # crée un tableau avec les différentes couleurs des voisins de la node
		for neighbor in node_neighbors:
			if neighbor in self.color_map:
				node_neighbors_color.append(self.color_map[neighbor]) #rentre dans le  tableau précédant les couleurs des nodes voisines
			else:
				uncolored_neighbors.append(neighbor)   # ajoute les nodes non colorés à la liste des nodes non-colorés et avec un/des voisin coloré
		uncolored_neighbors=list(set(uncolored_neighbors)) # enleve les doublons
		node_neighbors_color=list(set(node_neighbors_color)) # enlève les doublons
		print(node_neighbors,node_neighbors_color)
		#input()
		if len(node_neighbors_color)>=2: # test si la node ne touche de deja pas plus de 1 couleur
			print("node",node,"had too much colors touching it",node_neighbors_color)
			return False
		else:    #s'il n'y a pas de couleurs rattaché à la node on choisit la première couleur
			self.setnode_color(node,[x for x in self.two_color if x not in node_neighbors_color][0])    # change la couleur en la/les couleurs disponibles
			print("Colored",node,"in",[x for x in self.two_color if x not in node_neighbors_color][0])
		uncolored.remove(node)
		if node in uncolored_neighbors:
			uncolored_neighbors.remove(node)
	return True
```

