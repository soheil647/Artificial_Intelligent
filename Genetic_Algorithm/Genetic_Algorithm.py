from Individual import Individual
from Population import Population
from TextProcessing import TextProcessing
import string
import random
import numpy as np


class GeneticAlgorithm:
    def __init__(self, population_size, number_of_generations, mutation_rate, cross_chance, encoded_text):
        self.population_size = population_size
        self.number_of_generations = number_of_generations
        self.mutation_rate = mutation_rate
        self.cross_chance = cross_chance
        self.encoded_text = encoded_text

    @staticmethod
    def __crossover(individual1_passed, individual2_passed):
        child1 = dict.fromkeys(string.ascii_lowercase, 0)
        child2 = dict.fromkeys(string.ascii_lowercase, 0)
        used_alphabet_child1 = []
        used_alphabet_child2 = []

        for letter in string.ascii_lowercase:
            if random.uniform(0, 1) < 0.5:
                temp = individual1_passed
                individual1_passed = individual2_passed
                individual2_passed = temp
            if individual1_passed.mapped_alphabet[letter] not in child1.values():
                child1[letter] = individual1_passed.mapped_alphabet[letter]
                used_alphabet_child1.append(individual1_passed.mapped_alphabet[letter])
            else:
                child1[letter] = 'None'
            if individual2_passed.mapped_alphabet[letter] not in child2.values():
                child2[letter] = individual2_passed.mapped_alphabet[letter]
                used_alphabet_child2.append(individual2_passed.mapped_alphabet[letter])
            else:
                child2[letter] = 'None'

        unused_alphabet_child1 = list(set(string.ascii_lowercase) - set(used_alphabet_child1))
        unused_alphabet_child2 = list(set(string.ascii_lowercase) - set(used_alphabet_child2))
        # i = 0
        # j = 0
        for alphabet in string.ascii_lowercase:
            if child1[alphabet] == 'None':
                random_letter = random.randint(0, len(unused_alphabet_child1) - 1)
                child1[alphabet] = unused_alphabet_child1[random_letter]
                unused_alphabet_child1.remove(unused_alphabet_child1[random_letter])
                # i += 1
            if child2[alphabet] == 'None':
                random_letter = random.randint(0, len(unused_alphabet_child2)-1)
                child2[alphabet] = unused_alphabet_child2[random_letter]
                unused_alphabet_child2.remove(unused_alphabet_child2[random_letter])
                # j += 1
        return Individual(list(child1.values())), Individual(list(child2.values()))

    def mutation(self, individual):
        if random.uniform(0, 1) < self.mutation_rate:
            for letter in range(4):
                random_letter_1 = random.randint(0, 13)
                random_letter_2 = random.randint(13, 25)
                temp_letter = individual.mapped_alphabet[string.ascii_lowercase[random_letter_1]]
                individual.mapped_alphabet[string.ascii_lowercase[random_letter_1]] = individual.mapped_alphabet[string.ascii_lowercase[random_letter_2]]
                individual.mapped_alphabet[string.ascii_lowercase[random_letter_2]] = temp_letter
        return individual

    def tournament(self, generation):
        parents = []
        for number_of_parent in range(8):
            parents.append(random.choice(generation[:int(self.population_size)]))
        parents.sort(key=lambda x: x.fitness, reverse=True)
        return parents[0], parents[1]

    def evolve(self):
        my_text_object_global = TextProcessing(text="", text_file_address="Attachment/global_text.txt")
        # my_text_object_encoded = TextProcessing(text="", text_file_address="Attachment/encoded_text.txt")
        my_text_object_encoded = TextProcessing(text=self.encoded_text)
        text = my_text_object_encoded.text
        global_text = my_text_object_global.clean_text()
        encoded_text = my_text_object_encoded.clean_text()
        generation = Population(self.population_size, True)

        max_fitness = generation.find_max_fitness(encoded_text, global_text)
        for j in range(self.number_of_generations):
            if generation.get_individuals()[0].fitness != max_fitness:

                # print("Generation number: ", j)
                for chromosome in generation.get_individuals():
                    chromosome.calculate_fitness(global_text, encoded_text)

                generation.get_individuals().sort(key=lambda x: x.fitness, reverse=True)

                new_generation = generation.get_individuals()[:int(self.population_size * 0.1)]
                for i in range(int(self.population_size * 0.7)):
                    if random.uniform(0, 1) < self.cross_chance:
                        while True:
                            parent1, parent2 = random.choices(new_generation[:int(self.population_size * 0.8)], k=2)
                            if parent1 != parent2:
                                break
                        child1, child2 = self.__crossover(parent1, parent2)
                        child1 = self.mutation(child1)
                        child2 = self.mutation(child2)
                        new_generation.append(child1)
                        new_generation.append(child2)

                generation.save_individuals(new_generation)
                # print("Report Best Fitness: ", generation.get_individuals()[0].fitness)
                # print("Population number is:", len(generation.get_individuals()))
            else:
                break
        for chromosome in generation.get_individuals():
            chromosome.calculate_fitness(my_text_object_global.get_text(), my_text_object_encoded.get_text())
        generation.get_individuals().sort(key=lambda x: x.fitness, reverse=True)

        return generation.get_individuals()[0].decode_text(text)

