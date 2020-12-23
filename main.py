from coloration import *
from Graph import Graph

#a=[('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')]
a=[('A', 'B'), ('B', 'C'), ('B', 'D'),('A', 'E'),('A', 'F')]
G=Graph(a)
double_coloration_optimal(G)
G.show()
print("Check:",check_triple_coloration(G))