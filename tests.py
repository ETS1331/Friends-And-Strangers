from main import *
'''
#Example 1.1
G = Graph(3)
H = Graph(3)
G.Edge(1,2)
G.Edge(2,3)
H.Edge(1,2)
H.Edge(2,3)
combine(G,H)
'''
#Example 1.2
G = Graph(5)
H = Graph(5)
G.Edge(1,2)
G.Edge(2,3)
G.Edge(3,4)
G.Edge(4,5)
G.Edge(5,1)
H.Edge(1,2)
H.Edge(2,3)
H.Edge(3,4)
H.Edge(4,1)
H.Edge(1,3)
H.Edge(4,5)
combine(G,H)
