from Individual import Individual
from Population import Population
import string
import random


class GeneticAlgorithm:
    def __init__(self, population_size, number_of_generations, mutation_rate, tournament_size):
        self.population_size = population_size
        self.number_of_generations = number_of_generations
        self.mutation_rate = mutation_rate
        self.tournament_size = tournament_size

    # Randomly choose 8% of population and returns the fittest one
    # def tournament_selection(self):


    @staticmethod
    def


    @staticmethod
    def crossover(individual1_passed, individual2_passed):
        random_point = random.randint(0, len(individual1_passed.get_mapped_alphabet()))
        print(random_point)

        from_first_parent = list(individual1_passed.get_mapped_alphabet().values())[:random_point]
        from_second_parent = list(individual2_passed.get_mapped_alphabet().values())[random_point:]
        unused_alphabet_list = list(set(string.ascii_lowercase) - set(from_first_parent))

        i = 0
        for indx in range(len(from_second_parent)):
            if from_first_parent.__contains__(from_second_parent[indx]):
                from_second_parent[indx] = unused_alphabet_list[i]
                i += 1

        child = from_first_parent + from_second_parent
        individual1_created = Individual(child)
        print(individual1_created.get_mapped_alphabet())

    # def mutation(self):

    # def genetic_algorithm(self):
