from types import NoneType
import numpy as np
from math import e, sin
import random, sys

f = open(f"NN_T3_output_Test1.txt", "w")
def rand_n(): return round(np.random.uniform(0.0, 360.0), 3)
def sin_(x): return (sin(x) > 0)*1
def relU_(x): return max(0.0, x)
def sigmoid(x): return ((1 / (1 + e**(-x)))>0)*1
def direct(x): return x


functions_dict = {'relU': relU_, 'sin': sin_, 'direct': direct, 'sigmoid': sigmoid}

for x in functions_dict:
    functions_dict[x] = np.vectorize(functions_dict[x])

class NeuralNetwork:

    def __init__(self, no_neurons, gene, functions, bias=None):
        self.layers = np.array([np.array([0]*n, dtype=float)
                               for n in no_neurons], dtype=np.ndarray)
        self.weights = gene
        self.bias = bias
        self.functions = functions

    def forward(self, inp):
        self.layers[0] = inp
        for i, func in zip([i for i in range(1, len(self.layers))], self.functions):
            prev_layer = self.layers[i-1]
            mult_result = np.matmul(prev_layer, self.weights[i-1])
            if type(self.bias)!=NoneType:
                mult_result = np.add(mult_result, self.bias[i])
            self.layers[i] = functions_dict[func](mult_result)
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

