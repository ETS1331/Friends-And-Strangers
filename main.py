from re import L
import networkx as nx
import matplotlib.pyplot as plt
import math
from itertools import permutations
class Graph:
    def __init__(self,vertices):
        self.visual = []
        self.vertices = vertices #Please let this number be correct
    def Edge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)
    def visualize(self):
        G = nx.Graph() 
        G.add_edges_from(self.visual)
        plt.figure(1,figsize=(12,12)) 
        nx.draw_spring(G,font_size=8)
        plt.show()
def combine(G,H): #Create the friends and strangers graph based on the graphs
    if G.vertices != H.vertices: #Force equal number of vertices
        return None
    v = G.vertices
    I = Graph(math.factorial(v))
    k = permutations([i+1 for i in range(v)])
    k = list(k)
    for i in range(len(k)): 
        for a in range(1,v+1):
            for b in range(1,v+1):
                if  [a,b] in G.visual and [k[i][a-1],k[i][b-1]] in H.visual: #Swap Conditions! 
                    tmp = list(k[i])
                    tmp[a-1] = k[i][b-1]#ok maybe I should've just let a,b go from 0 to v-1 instead
                    tmp[b-1] = k[i][a-1] 
                    tmp = tuple(tmp)
                    I.Edge(k[i],tmp)
    I.visualize()
