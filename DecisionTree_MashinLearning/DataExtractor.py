import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from imblearn.over_sampling import RandomOverSampler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import datetime


class DataExtractor:
    def __init__(self, filepath):
        self.DataFrame = pd.read_csv(filepath, index_col=0)

    def split_labels(self, label_name="Is Back"):
        desired_width = 320
        pd.set_option('display.width', desired_width)
        pd.set_option('display.max_columns', 10)

        self.country_encode()
        self.date_get_day()
        self.scale_data()

        x = self.DataFrame.drop(label_name, axis=1)
        y = self.DataFrame[label_name]
        return x, y

    def split_validation(self, validation_rate=0.3):
        x, y = self.split_labels()
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=validation_rate, random_state=0)

        ros = RandomOverSampler(random_state=0)
        x_train, y_train = ros.fit_resample(x_train, y_train)

        return x_train, x_test, y_train, y_test

    def scale_data(self):
        # self.DataFrame = self.DataFrame.drop(self.DataFrame[(self.DataFrame['Total Quantity'] < 0)].index)
        # self.DataFrame = self.DataFrame.drop(self.DataFrame[(self.DataFrame['Total Price'] < 0)].index)
        # self.DataFrame['Total Quantity'] = self.DataFrame['Total Quantity'].where(self.DataFrame['Total Quantity'] < 0, self.DataFrame['Total Quantity'].mean())
        # self.DataFrame['Total Price'] = self.DataFrame['Total Price'].where(self.DataFrame['Total Price'] < 0, self.DataFrame['Total Price'].mean())
        scaler = StandardScaler()
        new_data = list(zip(self.DataFrame["Total Quantity"], self.DataFrame["Total Price"]))
        scaler.fit(new_data)
        new_data = scaler.transform(new_data)
        self.DataFrame["Total Quantity"] = new_data[:, 0]
        self.DataFrame["Total Price"] = new_data[:, 1]

    def country_encode(self):
        le = preprocessing.LabelEncoder()
        le.fit(self.DataFrame.Country)
        self.DataFrame.Country = le.transform(self.DataFrame.Country)

        # self.DataFrame = pd.concat([self.DataFrame, pd.get_dummies(self.DataFrame['Country'], prefix='Country', dummy_na=True)], axis=1).drop(['Country'], axis=1)

    def date_get_day(self):
        self.DataFrame.Date = self.DataFrame.Date.str.split('-').str[0] + self.DataFrame.Date.str.split('-').str[1] + self.DataFrame.Date.str.split('-').str[2]
        self.DataFrame.Date = pd.to_numeric(self.DataFrame.Date)

        # self.DataFrame.Date = pd.to_datetime(self.DataFrame.Date).dt.dayofweek
        # self.DataFrame.Date = pd.to_datetime(self.DataFrame.Date).dt.month + pd.to_datetime(self.DataFrame.Date).dt.day