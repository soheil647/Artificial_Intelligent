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
        return self.text.translate(str.maketrans('', '', string.punctuation))

    def drop_white_space(self):
        return self.text.strip()

    def tokenize_text(self):
        return nltk.word_tokenize(self.text)

    def drop_stop_words_and_tokenize(self):
        tokens = self.tokenize_text()
        return [i for i in tokens if i not in ENGLISH_STOP_WORDS]

    def do_stemming_and_tokenize(self):
        new_text = []
        stemmer = nltk.stem.PorterStemmer()
        tokens = self.tokenize_text()
        for word in tokens:
            new_text += stemmer.stem(word)
        return new_text

    def do_lemmatization(self):
        new_text = []
        lemmatizer = nltk.stem.WordNetLemmatizer()
        tokens = self.tokenize_text()
        for word in tokens:
            new_text += lemmatizer.lemmatize(word)
        return new_text

    def clean_text(self):
        self.text = self.drop_numbers()
        self.text = self.drop_punctuation()
        self.text = self.drop_stop_words_and_tokenize()
        with open('dictionary.txt', 'w') as f:
            for item in self.text:
                f.write("%s " % item)
        return self.text
