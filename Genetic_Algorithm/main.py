from TextProcessing import TextProcessing
from Individual import Individual
from Genetic_Algorithm import GeneticAlgorithm
from Population import Population
import string
import random
import time

# my_text_object_global = TextProcessing(text="", text_file_address="Attachment/global_text.txt")
# my_text_object_encoded = TextProcessing(text="", text_file_address="Attachment/encoded_text.txt")
# my_text_object_global.clean_text()
# my_text_object_encoded.clean_text()
# my_chromosome = Individual(string.ascii_lowercase)
# my_chromosome.calculate_fitness(my_text_object_global.get_text(), my_text_object_encoded.get_text())
# print(my_chromosome.fitness)
start_time = time.time()
ga = GeneticAlgorithm(50, 200, 0.6, 8)
ga.evolve()
print(time.time() - start_time)