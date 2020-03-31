from Individual import Individual
from Population import Population
from TextProcessing import TextProcessing
import string
import random
import numpy as np


class GeneticAlgorithm:
    def __init__(self, population_size, number_of_generations, mutation_rate, tournament_size):
        self.population_size = population_size
        self.number_of_generations = number_of_generations
        self.mutation_rate = mutation_rate
        self.tournament_size = tournament_size

    # Randomly choose 8% of population and returns the fittest one
    # def tournament_selection(self):

    @staticmethod
    def __create_child_from_parents(individual1_passed, individual2_passed, random_point, child_number):
        if child_number == 2:
            temp = individual1_passed
            individual1_passed = individual2_passed
            individual2_passed = temp

        from_first_parent = list(individual1_passed.get_mapped_alphabet().values())[:random_point]
        from_second_parent = list(individual2_passed.get_mapped_alphabet().values())[random_point:]
        unused_alphabet_list = list(set(string.ascii_lowercase) - set(from_first_parent))
        i = 0
        for indx in range(len(from_second_parent)):
            if from_first_parent.__contains__(from_second_parent[indx]):
                from_second_parent[indx] = unused_alphabet_list[i]
                i += 1
        return Individual(from_first_parent + from_second_parent)

    def crossover(self, individual1_passed, individual2_passed):
        random_point = random.randint(0, len(individual1_passed.get_mapped_alphabet()))
        child1 = self.__create_child_from_parents(individual1_passed, individual2_passed, random_point, 1)
        child2 = self.__create_child_from_parents(individual1_passed, individual2_passed, random_point, 2)
        return child1, child2

    # def mutation(self):

    def evolve(self):
        my_text_object_global = TextProcessing(text="", text_file_address="Attachment/global_text.txt")
        my_text_object_encoded = TextProcessing(text="", text_file_address="Attachment/encoded_text.txt")
        my_text_object_global.clean_text()
        my_text_object_encoded.clean_text()

        generation = Population(50, True)
        for j in range(self.number_of_generations):
            print("Generation number: " , j)
            # new_generation = []
            for chromosome in generation.get_individuals():
                chromosome.calculate_fitness(my_text_object_global.get_text(), my_text_object_encoded.get_text())

            generation.get_individuals().sort(key=lambda x: x.fitness, reverse=True)

            new_generation = generation.get_individuals()[:45]
            # print(new_generation)
            # print(np.array(new_generation).shape)
            for i in range(5):
                parent1, parent2 = random.choices(generation.get_individuals()[:20], k=2)
                # print("Parents are: ", parent1, parent2)
                child1, child2 = self.crossover(parent1, parent2)
                # print("Childs are: ", child1, child2)
                new_generation.append(child1)
                new_generation.append(child2)

            # print(new_generation)
            # print(np.array(new_generation).shape)
            generation.save_individuals(new_generation)

        for chromosome in generation.get_individuals():
            chromosome.calculate_fitness(my_text_object_global.get_text(), my_text_object_encoded.get_text())
        generation.get_individuals().sort(key=lambda x: x.fitness, reverse=True)
        for chromosome in generation.get_individuals():
            print(chromosome.fitness)