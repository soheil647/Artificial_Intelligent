import string


class Individual:
    def __init__(self, mapped_alphabet, fitness=0):
        self.fitness = fitness
        self.mapped_alphabet = dict(zip(string.ascii_lowercase, mapped_alphabet))
        self.alphabet_usage = dict.fromkeys(string.ascii_lowercase, 0)

    def get_mapped_alphabet(self):
        return self.mapped_alphabet

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

    def __find_each_word_common_letter(self, global_dictionary, encoded_dictionary):
        # common_letter_number_word_in_decode_list = []
        for encoded_word in encoded_dictionary:
            common_letter_number_word_in_global = []
            common_word = []
            for word in global_dictionary:
                i = 0
                common_letters = ''
                while i < len(encoded_word) == len(word) and i < len(word):
                    if encoded_word[i] == word[i]:
                        common_letters += encoded_word[i]
                        i += 1
                    else:
                        break
                common_word.append(common_letters)
                common_letter_number_word_in_global.append(i)
            for j in common_word[common_letter_number_word_in_global.index(max(common_letter_number_word_in_global))]:
                self.alphabet_usage[j.lower()] += 1
            # common_letter_number_word_in_decode_list.append(max(common_letter_number_word_in_global))
        # return common_letter_number_word_in_decode_list

    # def __find_fitness(self, common_letter_number_word_in_decode_list):
    #     for i in range(max(common_letter_number_word_in_decode_list) + 1):
    #         self.fitness += i * common_letter_number_word_in_decode_list.count(i)
    #     return self.fitness

    def __find_fitness(self, decoded_dictionary, global_dictionary):
        fitness = 0
        # word_legnths = [1]
        for decoded_word in decoded_dictionary:
            for global_word in global_dictionary:
                if decoded_word == global_word:
                    fitness += len(decoded_word) * 3
                    # word_legnths.append(len(decoded_word))
                    # break
        self.fitness = fitness
        return self.fitness

    def calculate_fitness(self, global_dictionary, encoded_dictionary):
        self.fitness = 0
        self.alphabet_usage = dict.fromkeys(string.ascii_lowercase, 0)
        decoded_text = self.decode_string_list(encoded_dictionary)
        # number_of_common_letter_list = self.__find_each_word_common_letter(global_dictionary, decoded_text)
        # self.__find_each_word_common_letter(global_dictionary, decoded_text)
        # return self.__find_fitness(number_of_common_letter_list)
        # self.fitness = sum(self.alphabet_usage.values())
        self.__find_fitness(decoded_text, global_dictionary)
        return self.fitness


