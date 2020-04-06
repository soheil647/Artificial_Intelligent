from Individual import Individual
from Population import Population
from TextProcessing import TextProcessing
import string
import random
import numpy as np


class GeneticAlgorithm:
    def __init__(self, population_size, number_of_generations, mutation_rate, cross_chance):
        self.population_size = population_size
        self.number_of_generations = number_of_generations
        self.mutation_rate = mutation_rate
        self.cross_chance = cross_chance


    # @staticmethod
    # def __create_child_from_parents(individual1_passed, individual2_passed, random_point, child_number):
    #     if child_number == 2:
    #         temp = individual1_passed
    #         individual1_passed = individual2_passed
    #         individual2_passed = temp
    #
    #     from_first_parent = list(individual1_passed.get_mapped_alphabet().values())[:random_point]
    #     from_second_parent = list(individual2_passed.get_mapped_alphabet().values())[random_point:]
    #     unused_alphabet_list = list(set(string.ascii_lowercase) - set(from_first_parent))
    #     i = 0
    #     for indx in range(len(from_second_parent)):
    #         if from_first_parent.__contains__(from_second_parent[indx]):
    #             from_second_parent[indx] = unused_alphabet_list[i]
    #             i += 1
    #     return Individual(from_first_parent + from_second_parent)
    #
    # def __crossover(self, individual1_passed, individual2_passed):
    #     random_point = random.randint(0, len(individual1_passed.get_mapped_alphabet()))
    #     child1 = self.__create_child_from_parents(individual1_passed, individual2_passed, random_point, 1)
    #     child2 = self.__create_child_from_parents(individual1_passed, individual2_passed, random_point, 2)
    #     return child1, child2

    # @staticmethod
    # def __crossover(individual1_passed, individual2_passed):
    #     child = dict.fromkeys(string.ascii_lowercase, 0)
    #     used_alphabet = []
    #     for letter in string.ascii_lowercase:
    #         if individual1_passed.alphabet_usage[letter] >= individual2_passed.alphabet_usage[letter] and individual1_passed.mapped_alphabet[letter] not in child.values():
    #             child[letter] = individual1_passed.mapped_alphabet[letter]
    #             used_alphabet.append(individual1_passed.mapped_alphabet[letter])
    #         elif individual2_passed.alphabet_usage[letter] >= individual1_passed.alphabet_usage[letter] and individual2_passed.mapped_alphabet[letter] not in child.values():
    #             child[letter] = individual2_passed.mapped_alphabet[letter]
    #             used_alphabet.append(individual2_passed.mapped_alphabet[letter])
    #         else:
    #             child[letter] = 'None'
    #     unused_alphabet = list(set(string.ascii_lowercase) - set(used_alphabet))
    #     i = 0
    #     for alphabet in string.ascii_lowercase:
    #         if child[alphabet] == 'None':
    #             child[alphabet] = unused_alphabet[i]
    #             i += 1
    #     return Individual(list(child.values()))

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
        i = 0
        j = 0
        for alphabet in string.ascii_lowercase:
            if child1[alphabet] == 'None':
                child1[alphabet] = unused_alphabet_child1[i]
                i += 1
            if child2[alphabet] == 'None':
                child2[alphabet] = unused_alphabet_child2[j]
                j += 1
        return Individual(list(child1.values())), Individual(list(child2.values()))

    # @staticmethod
    # def __crossover(individual1_passed, individual2_passed):
    #     child1 = dict.fromkeys(string.ascii_lowercase, 0)
    #     used_alphabet_child1 = []
    #
    #     for letter in string.ascii_lowercase:
    #         if random.uniform(0, 1) < 0.5:
    #             if individual1_passed.mapped_alphabet[letter] not in child1.values():
    #                 child1[letter] = individual1_passed.mapped_alphabet[letter]
    #                 used_alphabet_child1.append(individual1_passed.mapped_alphabet[letter])
    #             else:
    #                 child1[letter] = 'None'
    #         else:
    #             if individual2_passed.mapped_alphabet[letter] not in child1.values():
    #                 child1[letter] = individual2_passed.mapped_alphabet[letter]
    #                 used_alphabet_child1.append(individual2_passed.mapped_alphabet[letter])
    #             else:
    #                 child1[letter] = 'None'
    #
    #     unused_alphabet_child1 = list(set(string.ascii_lowercase) - set(used_alphabet_child1))
    #     i = 0
    #     for alphabet in string.ascii_lowercase:
    #         if child1[alphabet] == 'None':
    #             child1[alphabet] = unused_alphabet_child1[i]
    #             i += 1
    #     return Individual(list(child1.values()))

    # def mutation(self, individual):
    #     # for letter in range(5):
    #     if random.uniform(0, 1) < self.mutation_rate:
    #         random_letter_1 = random.randint(0, 13)
    #         random_letter_2 = random.randint(13, 25)
    #         temp_letter = individual.mapped_alphabet[string.ascii_lowercase[random_letter_1]]
    #         individual.mapped_alphabet[string.ascii_lowercase[random_letter_1]] = individual.mapped_alphabet[string.ascii_lowercase[random_letter_2]]
    #         individual.mapped_alphabet[string.ascii_lowercase[random_letter_2]] = temp_letter
    #     return individual

    def mutation(self, individual):
        for letter in range(5):
            if random.uniform(0, 1) < self.mutation_rate:
                random_letter_1 = random.randint(0, 12)
                random_letter_2 = random.randint(13, 25)
                values = list(individual.mapped_alphabet.values())
                copy = values[random_letter_1:random_letter_2]
                random.shuffle(copy)
                values[random_letter_1:random_letter_2] = copy
                # random.shuffle(values)
                individual.mapped_alphabet = dict(zip(string.ascii_lowercase, values))
        return individual

    # def mutation(self, individual):
    #     for letter in range(int(len(individual.mapped_alphabet)/2)):
    #         if random.uniform(0, 1) < self.mutation_rate:
    #             temp = individual.mapped_alphabet[string.ascii_lowercase[letter]]
    #             individual.mapped_alphabet[string.ascii_lowercase[letter]] = individual.mapped_alphabet[string.ascii_lowercase[-letter]]
    #             individual.mapped_alphabet[string.ascii_lowercase[-letter]] = temp
    #     return individual

    def tournament(self, generation):
        parents = []
        for number_of_parent in range(8):
            parents.append(random.choice(generation.get_individuals()[:int(self.population_size * 0.4)]))
        parents.sort(key=lambda x: x.fitness, reverse=True)
        return parents[0], parents[1]

    def evolve(self):
        my_text_object_global = TextProcessing(text="", text_file_address="Attachment/global_text.txt")
        my_text_object_encoded = TextProcessing(text="", text_file_address="Attachment/encoded_text.txt")
        global_text = my_text_object_global.clean_text()
        encoded_text = my_text_object_encoded.clean_text()
        print(global_text)
        print(encoded_text)
        generation = Population(self.population_size, True)
        # print(my_answer.decode_string_list(encoded_text))
        max_fitness = generation.find_max_fitness(encoded_text, global_text)
        # max_fitness = generation.find_max_fitness(encoded_text)
        print(max_fitness)
        for j in range(self.number_of_generations):
            if generation.get_individuals()[0].fitness != max_fitness:

                print("Generation number: ", j)
                for chromosome in generation.get_individuals():
                    chromosome.calculate_fitness(global_text, encoded_text)

                generation.get_individuals().sort(key=lambda x: x.fitness, reverse=True)

                new_generation = generation.get_individuals()[:int(self.population_size * 0.2)]
                for i in range(int(self.population_size * 0.5)):
                    if random.uniform(0, 1) < self.cross_chance:
                        while True:
                            parent1, parent2 = random.choices(new_generation[:int(self.population_size * 0.8)], k=2)
                            if parent1 != parent2:
                                break
                        child1, child2 = self.__crossover(parent1, parent2)
                        # child1 = self.__crossover(parent1, parent2)
                        child1 = self.mutation(child1)
                        child2 = self.mutation(child2)
                        new_generation.append(child1)
                        new_generation.append(child2)

                # for i in range(len(new_generation)):
                #     new_generation[i] = self.mutation(new_generation[i])

                generation.save_individuals(new_generation)
                print("Report Best Fitness: ", generation.get_individuals()[0].fitness)
                print("Population number is:", len(generation.get_individuals()))
            else:
                break
        for chromosome in generation.get_individuals():
            chromosome.calculate_fitness(my_text_object_global.get_text(), my_text_object_encoded.get_text())
        generation.get_individuals().sort(key=lambda x: x.fitness, reverse=True)
        for chromosome in generation.get_individuals():
            print(chromosome.fitness)

        for individual in generation.get_individuals():
            if individual.fitness == generation.get_individuals()[0].fitness:
                print(individual.decode_string_list(my_text_object_encoded.text))


        # print(generation.get_individuals()[0].alphabet_usage)
        # print(generation.get_individuals()[0].mapped_alphabet)
