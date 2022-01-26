from re import L
import networkx as nx
import matplotlib.pyplot as plt
import math
from itertools import permutations
class Graph:
    def __init__(self,vertices):
        self.edges = []
        
        self.G = nx.Graph()
        if type(vertices) == list:
            self.G.add_nodes_from(vertices)
            self.vertices = vertices
        else:
            self.G.add_nodes_from([i for i in range(vertices)])
            self.vertices = [i for i in range(vertices)]
    def edge(self, a, b):
        self.G.add_edge(a,b)
        self.edges.append([a,b])
    def visualize(self):
        plt.figure(1,figsize=(12,12)) 
        nx.draw_networkx(self.G)
        plt.show()
    def connected(self):
        print(nx.number_connected_components(self.G))
def combine(G,H): #Create the friends and strangers graph based on the graphs
    if len(G.vertices) != len(H.vertices): #Force equal number of vertices
        return None
    v = len(G.vertices)
    k = permutations([i+1 for i in range(v)])
    k = list(k)
    I = Graph(k)
    for i in range(len(k)): 
        for a in range(1,v+1):
            for b in range(1,v+1):
                if  [a,b] in G.edges and [k[i][a-1],k[i][b-1]] in H.edges: #Swap Conditions! 
                    tmp = list(k[i])
                    tmp[a-1] = k[i][b-1]#ok maybe I should've just let a,b go from 0 to v-1 instead
                    tmp[b-1] = k[i][a-1] 
                    tmp = tuple(tmp)
                    I.edge(k[i],tmp)
    return I
