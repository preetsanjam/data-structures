class Graph():
    def __init__(self):
        # Initialize an empty dictionary to store the graph
        # Keys = nodes, Values = list of neighboring nodes (adjacency list)
        self.graph={}
        
    def add_edge(self, node, neighbor):
        # If the node is not already in the graph, add it with an empty list
        if node not in self.graph:
            self.graph[node]=[]
        
        # Add the neighbor to the node's adjacency list
        self.graph[node].append(neighbor)