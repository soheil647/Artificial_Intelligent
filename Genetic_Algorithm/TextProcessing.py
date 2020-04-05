import re
import string
import nltk
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


class TextProcessing:
    def __init__(self, text="", text_file_address=""):
        if text != "":
            self.text = text
        if text_file_address != "":
            self.text = open(text_file_address, "r").read()

    def get_text(self):
        return self.text

    def drop_numbers(self):
        return re.sub(r'\d+', '', self.text)

    def drop_punctuation(self):
        my_punctuation = string.punctuation.replace("'", "")
        self.text = self.text.translate(str.maketrans(my_punctuation, ' ' * len(my_punctuation)))
        self.text = self.text.replace("'", "")
        return self.text

    def drop_white_space(self):
        return self.text.strip()

    def tokenize_text(self):
        return nltk.word_tokenize(self.text)

    def drop_stop_words_and_tokenize(self):
        tokens = self.tokenize_text()
        return [i for i in tokens if i not in ENGLISH_STOP_WORDS]

    def do_stemming(self, dictionary):
        new_text = []
        stemmer = nltk.stem.PorterStemmer()
        for word in dictionary:
            new_text += stemmer.stem(word)
        return new_text

    def do_lemmatization(self):
        new_text = []
        lemmatizer = nltk.stem.WordNetLemmatizer()
        tokens = self.tokenize_text()
        for word in tokens:
            new_text += lemmatizer.lemmatize(word)
        return new_text

    def remove_two_three_length_words(self):
        # my_list = list(self.text)
        # print(my_list)
        # print(len(my_list))
        # for i in range(len(my_list)):
        #     print(i)
        #     if len(my_list[i]) <= 5:
        #         # print(word)
        #         # while my_list.count(my_list[word]):
        #         #     my_list.remove(my_list[word])
        #         my_list.remove(my_list[i])
        # print(my_list)
        self.text = re.sub(r'\b\w{1,2}\b', '', self.text)
        return self.text

    def clean_text(self):
        self.text = self.drop_numbers()
        self.text = self.drop_punctuation()
        self.text = self.remove_two_three_length_words()
        self.text = self.drop_stop_words_and_tokenize()
        # self.text = self.tokenize_text()
        self.text = list(dict.fromkeys(self.text))

        return self.text
