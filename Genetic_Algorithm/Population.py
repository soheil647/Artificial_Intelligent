from Individual import Individual
import string
import random


class Population:

    def __init__(self, population_size, initialise=False):
        self.individuals = []

        # Creates the individuals
        if initialise:
            alphabet_list = list(string.ascii_lowercase)
            for i in range(population_size):
                random_alphabet = random.sample(alphabet_list, len(alphabet_list))
                self.individuals.append(Individual(mapped_alphabet=random_alphabet))

    def get_fitness(self, individual_passed, index=0):
        if index != 0:
            return self.individuals[index].fitness
        else:
            return individual_passed.fitness

    def fitness_of_the_fittest(self):
        fitness_of_the_fittest = self.get_fitness(self.get_fittest())
        return fitness_of_the_fittest

    def get_fittest(self):
        fittest = self.individuals[0]
        for i in range(len(self.individuals)):
            if self.get_fitness(fittest) <= self.get_fitness(self.individuals[i]):
                fittest = self.individuals[i]
        return fittest

    # @staticmethod
    # def find_max_fitness(encoded_dictionary):
        # max_fitness = 0
        # for size in range(max(len(x) for x in encoded_dictionary)):
        #     length_word = [item for item in encoded_dictionary if len(item) == size]
        #     max_fitness += len(length_word) * size

        # for word in encoded_dictionary:
        #     max_fitness += len(word)
        # alphabet_usage = dict.fromkeys(string.ascii_lowercase, 0)
        # for word in encoded_dictionary:
        #     for letter in word:
        #         alphabet_usage[letter.lower()] += 1
        # return sum(alphabet_usage.values())

    @staticmethod
    def find_max_fitness(encoded_dictionary, global_dictionary):
        my_list = ['o', 'r', 's', 'f', 'w', 'm', 'b', 't', 'i', 'k', 'g', 'h', 'k', 'n', 'v', 'e', 'l', 'p', 'd', 'j', 'c', 'u', 'y', 'q', 'a', 'x']
        my_answer = Individual(my_list)
        my_answer.calculate_fitness(global_dictionary, encoded_dictionary)
        return my_answer.fitness

    def size(self):
        return len(self.individuals)

    def get_individual(self, index):
        return self.individuals[index]

    def get_individuals(self):
        return self.individuals

    def save_individual(self, index, individual_passed):
        self.individuals[index] = individual_passed

    def save_individuals(self, individuals):
        self.individuals = individuals
