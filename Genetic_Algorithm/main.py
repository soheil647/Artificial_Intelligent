from Genetic_Algorithm import GeneticAlgorithm
import time


start_time = time.time()
ga = GeneticAlgorithm(50, 500, 0.2, 2)
ga.evolve()
print(time.time() - start_time)

