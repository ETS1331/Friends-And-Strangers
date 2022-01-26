from main import *
'''
#Example 1.1
G = Graph(3)
H = Graph(3)
G.edge(1,2)
G.edge(2,3)
H.edge(1,2)
H.edge(2,3)
FS = combine(G,H)
FS.visualize()
'''
#Example 1.2
G = Graph(5)
H = Graph(5)
G.edge(1,2)
G.edge(2,3)
G.edge(3,4)
G.edge(4,5)
G.edge(5,1)
H.edge(1,2)
H.edge(2,3)
H.edge(3,4)
H.edge(4,1)
H.edge(1,3)
H.edge(4,5)
FS = combine(G,H)
FS.connected()
FS.visualize()
