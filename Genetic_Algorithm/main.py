from TextProcessing import TextProcessing
from Individual import Individual
from Genetic_Algorithm import GeneticAlgorithm
import string
import random


# my_text_object_global = TextProcessing(text="", text_file_address="Attachment/global_text.txt")
# my_text_object_encoded = TextProcessing(text="", text_file_address="Attachment/encoded_text.txt")
# # print(my_text_object.clean_text())
#
lr = random.sample(string.ascii_lowercase, len(string.ascii_lowercase))
my_indiviual = Individual(lr)
lr2 = random.sample(string.ascii_lowercase, len(string.ascii_lowercase))
my_indiviual2 = Individual(lr2)
print(my_indiviual.get_mapped_alphabet())
print(my_indiviual2.get_mapped_alphabet())
# print(list(my_indiviual.get_mapped_alphabet().values())[2])

GA = GeneticAlgorithm(10,10,0.2,5)
GA.crossover(my_indiviual,my_indiviual2)

# print(my_indiviual.calculate_fitness(my_text_object_global.clean_text(), my_text_object_encoded.clean_text()))
# print(my_text_object_encoded.text)
# print(my_text_object_global.text)