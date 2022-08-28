import numpy as np
from tqdm import tqdm
from math import e, sin
import random, sys

class NeuralNetwork:
	def __init__(self, gene):
		self.X = 0
		self.X_weights = np.array(gene[0], dtype=float)
		self.A = np.array([0,0], dtype=float)
		self.A_weights = np.array(gene[1],dtype=float)
		self.C = np.array([0]*3, dtype =float)
		self.C_weights = np.array(gene[2], dtype=float)
		self.E = np.array([0, 0], dtype =float)

	def forward(self, inp):
		res = -1
		self.X = inp
		self.A = self.X*self.X_weights
		self.C = forward_step(self.A,self.A_weights)
		self.E = forward_step(self.C,self.C_weights)
		self.E = [actiavtion(self.E[0]),actiavtion(self.E[0])]
		if self.E[0]>=0.5 and self.E[1]<0.5: 
			res = 1
		elif self.E[1]>0.5 and self.E[0]<0.5:
			res = 0 
		return res

def actiavtion(z):
	try:
		return sin(z)
	except:
		return -1


def forward_step(L, L_weight):
	X = np.matmul(L,L_weight)
	for i in range(len(X)):
		X[i]=actiavtion(X[i])
	return X

def raw_fitness_func(inp, res):
	return inp&1==res

def random_gene():
	
	res_0, res_1, res_2 = [], [], []
	for _ in range(2): res_0.append(np.random.uniform(-100,100))
	for _ in range(2): res_1.append([np.random.uniform(-100,100),np.random.uniform(-100,100),np.random.uniform(-100,100)])
	for _ in range(3): res_2.append([np.random.uniform(-100,100),np.random.uniform(-100,100)])
	return [res_0,res_1, res_2]


ITS = 500


def fitness_func(gene):
	curr_sum = 0
	NN = NeuralNetwork(gene)
	for _ in range(ITS):
		inp = random.randint(1, 500)
		curr_sum += raw_fitness_func(inp, NN.forward(inp))
	del NN
	return curr_sum

def run_generations():
	solutions = [random_gene() for _ in range(ITS)]
	
	def mutate(k, change_range):
		for i in range(len(gene[k])):
				for j in range(len(gene[k][0])):
					gene[k][i][j]*=random.uniform(change_range[0],change_range[1])
	
	for i in range (ITS):
		rankedsolutions = []

		for j in tqdm(range(len(solutions))):
			gene  = solutions[j]
			rankedsolutions.append((fitness_func(gene), gene))
		rankedsolutions.sort(reverse=True)
		print(f"=== Gen {i} best solutions === ")
		print("fitness :", rankedsolutions[0][0])
		
		if rankedsolutions[0][0]>180:
			print(rankedsolutions[0])
			break
		if i>190:
			print(f"------->  {i}    :   {rankedsolutions[0]}")

		bestsolutions = rankedsolutions [:50]
		newGen=[]
		for k in range (ITS):
			gene_fitness = random.choice(bestsolutions)
			gene = gene_fitness[1]
			fitness = gene_fitness[0]
			if not fitness:
				change_range=(0.0004, 500)
			elif fitness<ITS/2:
				change_range = (0.5, 1.5)
			elif fitness<ITS*0.70:
				change_range = (0.8, 1.2)
			else:
				change_range = (0.98, 1.02)

			for k in range(1,3):
				mutate(k,change_range)
			
			newGen.append(gene)

		solutions = newGen


# print("A for running generations, B for running test")
# if input()=='A':
# 	run_generations()
# else:
# 	run_test()

# run_generations()

run_generations()