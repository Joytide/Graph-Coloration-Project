from coloration import *
from Graph import Graph

from string import ascii_uppercase as alphabet

def graph_generator(n,p):
	from networkx.generators.random_graphs import fast_gnp_random_graph
	return Graph(fast_gnp_random_graph(n,p).edges)

g=graph_generator(35,0.1)
triple_coloration(g)
g.show()

"""
#Graph colorable avec 2 couleurs
two_colorable=Graph([('A', 'B'), ('B', 'C'), ('B', 'D'),('A', 'E'),('A', 'F')])
double_coloration_optimal(two_colorable)
two_colorable.show()

#Graph non colorable avec 2 couleurs
three_colorable=Graph([('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')])
double_coloration_optimal(three_colorable)
three_colorable.show()
triple_coloration(three_colorable)
three_colorable.show()

print("Verification:",check_triple_coloration(three_colorable))

not_three_colorable=Graph([('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('C', 'D'),('B', 'D')])
triple_coloration(not_three_colorable)
not_three_colorable.show()

print("Verification:",check_triple_coloration(not_three_colorable))
"""