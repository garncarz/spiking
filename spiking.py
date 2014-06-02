import numpy as np
import numpy.random as rnd

class Net:

	groupCount = 3
	neuronCount = 10
	synapsisCount = 20

	def __init__(self):
		self.weights = np.zeros((self.neuronCount, self.neuronCount))
		for i in range(self.synapsisCount):
			self.weights[rnd.randint(self.neuronCount)] \
				[rnd.randint(self.neuronCount)] = rnd.rand()
		
		self.tresholds = rnd.random_sample(self.neuronCount)
		# self.values = np.zeros(self.neuronCount)
		self.values = rnd.random(self.neuronCount)
		
		self.groups = rnd.randint(self.groupCount, size = self.neuronCount)
		self.inputs = filter(lambda neuron: self.groups[neuron] == 0,
			range(self.neuronCount))
		self.outputs = filter(lambda neuron:
			self.groups[neuron] == self.groupCount - 1, range(self.neuronCount))

	
	def step(self):
		self.randomInputs()
		self.valuesNext = np.copy(self.values)
		
		for neuron in range(self.neuronCount):
			if self.values[neuron] < self.tresholds[neuron]:
				continue
			# else fire and reset:
			for dest in range(self.neuronCount):
				self.valuesNext[dest] += self.weights[neuron][dest] * \
					self.values[neuron]
			self.valuesNext[neuron] -= self.values[neuron]
		
		self.values = self.valuesNext

	def randomInputs(self):
		for neuron in self.inputs:
			self.values[neuron] = rnd.random()
	
	
	def printOutputs(self):
		print(", ".join(map(lambda neuron: str(self.values[neuron]),
			self.outputs)))
	

