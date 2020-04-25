import string


class Individual:
    def __init__(self, mapped_alphabet, fitness=0):
        self.fitness = fitness
        self.mapped_alphabet = dict(zip(string.ascii_lowercase, mapped_alphabet))

    def get_mapped_alphabet(self):
        return self.mapped_alphabet

    def decode_text(self, text):
        new_text = ""
        print(text)
        for letter in text:
            new_word = ""
            if letter.isupper():
                letter = self.mapped_alphabet[letter.lower()].upper()
            if letter.islower():
                letter = self.mapped_alphabet[letter]
            new_word += letter
            new_text += new_word
        return new_text

    def decode_string_list(self, encoded_dictionary):
        new_text = []
        for word in encoded_dictionary:
            new_word = ""
            for letter in word:
                if letter.isupper():
                    letter = self.mapped_alphabet[letter.lower()].upper()
                if letter.islower():
                    letter = self.mapped_alphabet[letter]
                new_word += letter
            new_text.append(new_word)
        return new_text

    def __find_fitness(self, decoded_dictionary, global_dictionary):
        fitness = 0
        for decoded_word in decoded_dictionary:
            for global_word in global_dictionary:
                if decoded_word == global_word:
                    fitness += 1
        self.fitness = fitness
        return self.fitness

    def calculate_fitness(self, global_dictionary, encoded_dictionary):
        self.fitness = 0
        decoded_text = self.decode_string_list(encoded_dictionary)
        self.__find_fitness(decoded_text, global_dictionary)
        return self.fitness


