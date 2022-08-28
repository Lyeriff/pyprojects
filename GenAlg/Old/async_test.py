import asyncio
from NeuralObject import *

gene3 = [[[65.424, 18.3, -78.54]], [[-85.625, 67.831, -90.7, 74.675], [-79.959, 84.099, -98.033, 6.779], [-38.91, -16.928, 77.09, 30.788]], [[94.925, 68.913, 75.07], [-8.949, 61.567, -34.232], [26.923, -29.514, 43.075], [23.307, -83.251, 3.387]], [[-85.434], [57.135], [-79.363]]]
NN = NeuralNetwork([1,3,4,3,1], gene3, sin_)
async def test(inp):
    return NN.forward([inp])[0]==inp&1

async def run_(n):
    for _ in range(n):
        n+=await test(np.random.randint(1,100000))
    return n

async def main():
    x=await run_(100)
    print(x)

asyncio.run(main())