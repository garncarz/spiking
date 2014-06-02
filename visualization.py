import networkx as nx
import matplotlib.pyplot as plt

class NetVisualization:

	def __init__(self, net):
		self.net = net
	
	
	def show(self):
		graph = nx.DiGraph()
		for orig in range(self.net.neuronCount):
			for dest in range(self.net.neuronCount):
				if self.net.weights[orig][dest]:
					graph.add_edge(orig, dest,
						weight = self.net.weights[orig][dest])
		values = [self.net.values[node] for node in graph.nodes()]
		nx.draw(graph, cmap = plt.get_cmap("Purples"), node_color = values)
		plt.show()

