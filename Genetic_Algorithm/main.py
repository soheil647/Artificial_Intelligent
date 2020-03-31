from TextProcessing import TextProcessing
from Individual import Individual
from Genetic_Algorithm import GeneticAlgorithm
from Population import Population
import string
import random
import time


ga = GeneticAlgorithm(50, 10, 1, 8)
ga.evolve()