from DataExtractor import DataExtractor
from TextProcessing import TextProcessing
from TextClassifier import TextClassifier
import pandas as pd

train, target = DataExtractor('data.csv').data_producer('train')
test = DataExtractor('test.csv').data_producer('test')

text_classifier = TextClassifier()

(x_train, y_train), (x_validation, y_validation) = text_classifier.split_validation_data(train, target)

cleaned_x_train = TextProcessing(x_train).clean_text()
cleaned_x_validation = TextProcessing(x_validation).clean_text()
cleaned_x_test = TextProcessing(test).clean_text()

text_classifier.fit(cleaned_x_train, y_train)

text_classifier.evaluate(cleaned_x_validation, y_validation)

text_classifier.confusion(y_train, cleaned_x_train)


result = text_classifier.predict(cleaned_x_test)
pd.DataFrame(result, columns=['category']).to_csv('output.csv', index=True, index_label='index')
