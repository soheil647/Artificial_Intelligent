import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


class DataExtractor:
    def __init__(self, filepath):
        self.DataFrame = pd.read_csv(filepath, index_col=0).drop('Customer ID', axis=1)

    def split_labels(self, label_name="Is Back"):

        le = preprocessing.LabelEncoder()
        le.fit(self.DataFrame.Country)
        self.DataFrame.Country = le.transform(self.DataFrame.Country)

        self.DataFrame.Date = self.DataFrame.Date.str.split('-').str[1] + self.DataFrame.Date.str.split('-').str[2]
        self.DataFrame.Date = pd.to_numeric(self.DataFrame.Date)

        x = self.DataFrame.drop(label_name, axis=1)
        y = self.DataFrame[label_name]
        return x, y

    def split_validation(self, validation_rate=0.4):
        x, y = self.split_labels()
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=validation_rate)
        return x_train, x_test, y_train, y_test