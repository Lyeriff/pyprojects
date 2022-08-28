from tqdm import tqdm
import numpy as np
from math import e, sin
import random
import sys
import asyncio

rand_n = lambda: round(np.random.uniform(-180.0, 180.0), 3)
sin_ = lambda x: (sin(x) > 0)*1


class NeuralNetwork:

	def __init__(self, no_neurons, gene, activation_func):
		self.layers = np.array([np.array([0]*n, dtype=float)
		                       for n in no_neurons], dtype=np.ndarray)
		self.weights = gene
		self.activation = np.vectorize(activation_func)

	def forward(self, inp):
		self.layers[0] = inp
		for i in range(1, len(self.layers)):
			prev_layer = self.layers[i-1]
			self.layers[i] = self.activation(np.matmul(prev_layer, self.weights[i-1]))
		return self.layers[-1]


def random_gene(dimensions):
	res = []
	for k in range(len(dimensions)-1):
		i = dimensions[k]
		curr_gene = []
		for j in range(i):
			curr_neuron_weights = []
			for l in range(dimensions[k+1]):
				curr_neuron_weights.append(rand_n())
			curr_gene.append(curr_neuron_weights)
		res.append(curr_gene)
	return res


def mutate_float(x, range):
	return x*np.random.uniform(range[0], range[1])


def mutate_gene(item, range):
    if isinstance(item, list):
        return [mutate_gene(x, range) for x in item]
    else:
        return mutate_float(item, range)


ITS = 350
dimensions = [1, 3, 4, 5, 6, 4, 1]


async def test(NN, inp):
    return NN.forward([inp])[0] == inp & 1


async def fitness_func(gene):
    NN = NeuralNetwork(dimensions, gene, sin_)
    sum_0 = 0
    for _ in range(ITS):
        inp = np.random.randint(1, 100000)
        sum_0 += await test(NN, inp)
    return sum_0


async def run_generations():
    solutions = [random_gene(dimensions) for _ in range(ITS)]
    for i in range(ITS):
        rankedsolutions = []
        for j in tqdm(range(len(solutions))):
            gene = solutions[j]
            fitness = await fitness_func(gene)
            rankedsolutions.append((fitness, gene))
        rankedsolutions.sort(reverse=True)
        print(f"=== Gen {i} best solutions === ")
        print("fitness :", rankedsolutions[0][0])
        
        if rankedsolutions[0][0]>ITS*0.99:
            print(rankedsolutions[0])
            break
        if i>50:
            print(f"------->  {i}    :   {rankedsolutions[0]}")
        
        bestsolutions = rankedsolutions [:50]
        newGen=[i[1] for i in bestsolutions]
        for k in range (ITS-50):
            gene_fitness = random.choice(bestsolutions)
            gene = gene_fitness[1]
            fitness = gene_fitness[0]
            change_range = [0.98, 1.02]
            
            gene = mutate_gene(gene, change_range)
            
            newGen.append(gene)
        
        solutions = newGen
asyncio.run(run_generations())