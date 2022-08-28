import random


def func(x, y, z):
	return 3*x**2 + 5*y**3 -7


def fitness (x, y, z):
	ans = func (x, y, z)
	if ans == 0:
		return 99999
	else:
		return abs (1/ans)

def run_generations():
	solutions = []
	for s in range (1000):
		solutions.append((random.uniform(-1000, 1000),
		random.uniform(-1000, 1000),
		random.uniform(-1000, 1000)))

	for i in range (10000):

		rankedsolutions = []

		for s in solutions:
			rankedsolutions.append((fitness(s[0],s[1],s[2]),s))
		
		rankedsolutions.sort(reverse=True)
		print(f"=== Gen {i} best solutions === ")
		print(rankedsolutions [0])
		
		if rankedsolutions[0][0]> 999999
		: 
			return rankedsolutions[0][1]
			break

		bestsolutions = rankedsolutions [:100]
		elements = []
		for s in bestsolutions:
			elements.append(s[1][0])
			elements.append(s[1][1])
			elements.append(s[1][2])

		newGen = []
		for _ in range (1000):
			e1 = random.choice(elements)*random.uniform(0.98, 1.00)
			e2 = random.choice(elements)*random.uniform(0.99, 1.01)
			e3 = random.choice (elements)*random.uniform(0.98, 1.01)
			newGen.append((e1,e2, e3))
		solutions = newGen


def run_test(RES):
	print("==============================================")
	print(*RES)
	x, y, z = RES

	print(f"Test Output :  {func(x,y,z)}")
	print(f"Test Output rounded to 10 digits :  {round(func(x,y,z),10)}")

# print("A for running generations, B for running test")
# if input()=='A':
# 	run_generations()
# else:
# 	run_test()


run_test(run_generations())