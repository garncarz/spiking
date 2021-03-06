import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation

class NetVisualization:

	def __init__(self, net):
		self.net = net
		
		self.graph = nx.DiGraph()
		self.pos = {}
		for orig in range(self.net.neuronCount):
			self.pos[orig] = (self.net.groups[orig], orig)
			for dest in range(self.net.neuronCount):
				if self.net.weights[orig][dest]:
					self.graph.add_edge(orig, dest,
						weight = self.net.weights[orig][dest])
		#self.pos = nx.spring_layout(self.graph)
	
	
	def draw(self):
		values = [self.net.values[node] for node in self.graph.nodes()]
		plt.clf()
		nx.draw(self.graph, pos = self.pos,
			cmap = plt.get_cmap("Purples"), node_color = values)
	
	def drawNext(self):
		self.net.step()
		self.draw()

	
	def createGif(self, filename):
		fig = plt.figure()
		anim = animation.FuncAnimation(fig, lambda i: self.drawNext(),
			frames = 10)
		anim.save(filename, writer = "imagemagick", fps = 1)

