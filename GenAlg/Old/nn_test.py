import numpy as np
import

GENE =  [[[-1.0395735474816935e-115, -1.1650927404984248e-97, 8.553892976713376e-112], [5.3803599988265665e-127, -7.55808514357991e-122, -8.158470926011159e-113], [0.6870713558910251, 1.156093139600919, 0.5729764628609757]], [[1.5235786569846464e-104, -6.556481203970068e-130, -1.5059298392820166e-108], [-3.3780227465384955e-109, -4.765639126723591e-120, 8.191666652936935e-111]]]



class NuralNetwork:
	def __init__(self, gene):
		self.A = np.array([0,0,0])
		self.A_weights = np.array(gene[0],dtype=float)
		self.C = np.array([0]*3, dtype =float)
		self.C_weights = np.array(gene[1], dtype=float)
		self.E = np.array([0, 0], dtype =float)

	def forward(self, inp):
		self.A = np.array(inp)
		for i in range(3):
			self.C[i] = sum(self.A * self.A_weights[i])

		# print(self.C)
		for i in range(2):
			self.E[i] = sum(self.C * self.C_weights[i])
		# print(self.E)

		return self.E



def raw_fitness_func(inp, E):
	if sum(inp)&1:
		if E[0]>1 and E[1]<0: return 0
		else: return 1
	else:
		if E[0]<1 and E[1]>0: return 0
		else: return 1

def random_gene():
	
	res_0, res_1 = [], []
	for _ in range(3): res_0.append([np.random.uniform(-0.98,1.2),np.random.uniform(-0.98,1.2),np.random.uniform(-0.98,1.2)])
	for _ in range(2): res_1.append([np.random.uniform(-0.98,1.2),np.random.uniform(-0.98,1.2),np.random.uniform(-0.98,1.2)])
	return [res_0,res_1]

NN = NuralNetwork(GENE)
print("Actual : Predicted")
for _ in range(1000):
	inp = np.random.randint(1, 500, size=3)
	predicted_output = NN.forward(inp)
	actual_output = sum(inp)&1
	print(actual_output,"-------" ,predicted_output)
	# if predicted_output!=actual_output: print("WRONG")


