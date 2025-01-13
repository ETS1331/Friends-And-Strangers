from main import *
n = 4
G = Graph(n)
H = Graph(n)
for i in range(1,n):
    G.edge(0,i)
H.edge(0,1)
H.edge(1,2)
H.edge(2,3)
H.edge(0,3)
H.edge(1,3)
F = combine(G,H)
z = F.connected()
if len(z) == 1:
    print(F.diameter())
else:
    print('not connected', len(z))
