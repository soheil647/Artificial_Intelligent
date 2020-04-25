import pandas as pd


class DataExtractor:
    def __init__(self, data_file_path):
        self.data_frame = pd.read_csv(data_file_path)

    def data_producer(self, type_of_data):
        data = self.data_frame['headline'].fillna('') + ' ' + self.data_frame['short_description'].fillna('')
        if type_of_data == 'train':
            target = self.data_frame["category"]
            return data, target
        else:
            return data
