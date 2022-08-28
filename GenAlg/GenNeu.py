from tqdm import tqdm
from NeuralObject import *
ITS = 100
dimensions = [1,3,4,3,1]

def fitness_func(gene):
    NN = NeuralNetwork(dimensions, gene, sin_)
    sum_0=0
    for _ in range(100):
        inp = [np.random.randint(1,300)]
        out = NN.forward(inp)[0]
        if inp[0]&1 and out:
            sum_0+=1
        elif not inp[0]&1 and not out:
            sum_0+=1
        else:
            sum_0-=1
    return sum_0/100



    

def run_generations():
	solutions = [random_gene(dimensions) for _ in range(ITS)]
	
	for i in range (ITS):
		rankedsolutions = []
		for j in tqdm(range(len(solutions))):
			gene  = solutions[j]
			rankedsolutions.append((fitness_func(gene), gene))
		rankedsolutions.sort(reverse=True)
		print(f"=== Gen {i} best solutions === ")
		print("fitness :", rankedsolutions[0][0])
		
		if rankedsolutions[0][0]>95:
			print(rankedsolutions[0])
			break
		if i>95:
			print(f"------->  {i}    :   {rankedsolutions[0]}")

		bestsolutions = rankedsolutions [:40]
		newGen=[]
		for k in range (ITS):
			gene_fitness = random.choice(bestsolutions)
			gene = gene_fitness[1]
			fitness = gene_fitness[0]
			if not fitness:
				change_range=[0.0004, 500]
			elif fitness<ITS/2:
				change_range = [0.5, 1.5]
			elif fitness<ITS*0.70:
				change_range = [0.8, 1.2]
			else:
				change_range = [0.98, 1.02]

			gene = mutate_gene(gene, change_range)
			
			newGen.append(gene)

		solutions = newGen
run_generations()