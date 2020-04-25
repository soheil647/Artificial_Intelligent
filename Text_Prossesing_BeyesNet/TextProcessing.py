from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer


class TextProcessing:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    @staticmethod
    def __lemmatize_text(text):
        lemmatizer = WordNetLemmatizer()
        return [lemmatizer.lemmatize(w) for w in text]

    @staticmethod
    def __stemming_text(text):
        stemmer = PorterStemmer()
        return [stemmer.stem(w) for w in text]

    def __text_lower_case(self):
        self.data_frame = self.data_frame.str.lower()

    def __remove_numbers(self):
        self.data_frame = self.data_frame.str.replace('\d+', '')

    def __remove_punctuation(self):
        self.data_frame = self.data_frame.str.replace('[^\w\s]', '')

    def __remove_stop_words(self):
        stop_word = stopwords.words('english')
        self.data_frame = self.data_frame.apply(lambda x: [item for item in x.split() if item not in stop_word])

    def __do_lemmatization(self):
        self.data_frame = self.data_frame.apply(self.__lemmatize_text)

    def __do_stemming(self):
        self.data_frame = self.data_frame.apply(self.__stemming_text)

    def clean_text(self):
        self.__text_lower_case()
        self.__remove_numbers()
        self.__remove_punctuation()
        self.__remove_stop_words()
        self.__do_stemming()
        # self.__do_lemmatization()
        return self.data_frame
