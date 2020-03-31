import string


class Individual:
    def __init__(self, mapped_alphabet, fitness=0):
        self.fitness = fitness
        self.mapped_alphabet = dict(zip(string.ascii_lowercase, mapped_alphabet))

    def get_mapped_alphabet(self):
        return self.mapped_alphabet

    def __decode_string_list(self, encoded_dictionary):
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

    @staticmethod
    def __find_each_word_common_letter(global_dictionary, encoded_dictionary):
        common_letter_number_word_in_decode_list = []
        for encoded_word in encoded_dictionary:
            common_letter_number_word_in_global = []
            for word in global_dictionary:
                i = 0
                while i < len(encoded_word) and i < len(word):
                    if encoded_word[i] == word[i]:
                        i += 1
                    else:
                        break
                common_letter_number_word_in_global.append(i)
            common_letter_number_word_in_decode_list.append(max(common_letter_number_word_in_global))
        return common_letter_number_word_in_decode_list

    def __find_fitness(self, common_letter_number_word_in_decode_list):
        for i in range(max(common_letter_number_word_in_decode_list) + 1):
            self.fitness += i * common_letter_number_word_in_decode_list.count(i)
        return self.fitness

    def calculate_fitness(self, global_dictionary, encoded_dictionary):
        self.fitness = 0
        decoded_text = self.__decode_string_list(encoded_dictionary)
        number_of_common_letter_list = self.__find_each_word_common_letter(global_dictionary, decoded_text)
        return self.__find_fitness(number_of_common_letter_list)
