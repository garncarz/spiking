import numpy as np
import numpy.random as rnd

class Net:

	neuronCount = 10
	synapsisCount = 30

	def init(self):
		self.weights = np.zeros((self.neuronCount, self.neuronCount))
		for i in range(self.synapsisCount):
			self.weights[rnd.randint(self.neuronCount)] \
				[rnd.randint(self.neuronCount)] = rnd.rand()
		
		self.tresholds = rnd.random_sample(self.neuronCount)
		self.values = np.zeros(self.neuronCount)

