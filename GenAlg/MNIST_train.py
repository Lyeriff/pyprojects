from tqdm import tqdm
import numpy as np
from math import e, sin
import random
import asyncio

from mnist import MNIST
mndata = MNIST('./samples')
mndata.gz = True
images, labels = mndata.load_training()
images_slice, labels_slice = images[:500], labels[:500]



f = open(f"NN_output_Test1.txt", "w")
def rand_n(): return round(np.random.uniform(0.0, 360.0), 3)
def sin_(x): return (sin(x) > 0)*1
def relU_(x): return max(0.0, x)
def sigmoid(x): return ((1 / (1 + e**(-x)))>0)*1
def direct(x): return x


functions_dict = {'relU': relU_, 'sin': sin_, 'direct': direct, 'sigmoid': sigmoid}

for x in functions_dict:
    functions_dict[x] = np.vectorize(functions_dict[x])

class NeuralNetwork:

    def __init__(self, no_neurons, gene, functions):
        self.layers = np.array([np.array([0]*n, dtype=float)
                               for n in no_neurons], dtype=np.ndarray)
        self.weights = gene
        self.functions = functions

    def forward(self, inp):
        self.layers[0] = inp
        for i, func in zip([i for i in range(1, len(self.layers))], self.functions):
            prev_layer = self.layers[i-1]
            self.layers[i] = functions_dict[func](np.matmul(prev_layer, self.weights[i-1]))
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
    return np.array(res, dtype=object)


def mutate_float(x, range):
    return np.multiply(x,np.random.uniform(range[0], range[1]))


def mutate_gene(item, range):
    if not isinstance(item, float):
        return [mutate_gene(x, range) for x in item]
    else:
        return mutate_float(item, range)

def return_range(fitness, ITS):
    if fitness<ITS/5:
        res = [0.4, 2.5]
    elif fitness<ITS/4:
        res = [0.6, 1.6]
    elif fitness<ITS/2:
        res = [0.9, 1.1]
    else:
        res = [0.98, 1.02]
    return res

ITS = 100
dimensions = [784, 24, 16, 10]
functions = ['sin', 'sin', 'direct']


async def return_outputlayer(NN, inp):
    a = NN.forward(inp)
    return np.where(np.isclose(a, max(a)))[0][0]


async def fitness_func(gene):
    NN = NeuralNetwork(dimensions, gene, functions)
    sum_0 = 0
    for i in range(ITS//2):
        inp = images_slice[i]
        val = await return_outputlayer(NN, inp)
        sum_0 += val==labels_slice[i]
        if not i%10: print("\n")
        print(val, labels_slice[i], end =" ")
    
    return sum_0


# print(NN.forward([np.random.randint(0,2) for _ in range(784)]))

async def run_generations():
    solutions = [random_gene(dimensions) for _ in range(ITS)]
    for i in range(ITS):
        rankedsolutions = []
        for j in tqdm(range(len(solutions))):
            gene = solutions[j]
            fitness = await fitness_func(gene)
            rankedsolutions.append((fitness, gene))
        rankedsolutions= sorted(rankedsolutions, key=lambda x: x[0], reverse=True)
        print(f"\n=== Gen {i} best solutions === \n")
        print("fitness : ", rankedsolutions[0][0])

        f.write(f"\n\n-------> GEN -- {i}  {rankedsolutions[0][0]}\n\n")

        if i == ITS-1 or i==ITS-2:
            f.write("\n\n\n--------------------------------------------------------------------------\n\n")
            f.write(f"\n\n\n---------------------------------FINAL GENES --{i}-------------------------------------\n\n\n\n")
            f.write(f"{rankedsolutions[0]}")

        # if rankedsolutions[0][0] > ITS*0.99:
        #     print(rankedsolutions[0])
        #     break

        bestsolutions = rankedsolutions[:20]
        newGen = [i[1] for i in bestsolutions]
        for k in range(ITS-20):
            gene_fitness = random.choice(bestsolutions)
            gene = gene_fitness[1]
            fitness = gene_fitness[0]
            change_range = [0.99, 1.02]

            gene = mutate_gene(gene, change_range)

            newGen.append(gene)

        solutions = newGen
asyncio.run(run_generations())
